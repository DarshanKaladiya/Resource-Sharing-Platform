from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Course, Resource, Enrollment, Notification, User
from .form import SignUpForm, CourseForm, ResourceForm, SearchForm

# ... (home, signup, course_list, course_detail views remain the same) ...
def home(request):
    if request.user.is_authenticated:
        return redirect('classroom:course_list')
    return render(request, 'classroom/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            if role == 'mentor':
                group, created = Group.objects.get_or_create(name='Mentors')
                user.groups.add(group)
            else:
                group, created = Group.objects.get_or_create(name='Students')
                user.groups.add(group)
            login(request, user)
            return redirect('classroom:course_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'classroom/course_list.html', {'courses': courses})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    is_enrolled = course.enrolled_students.filter(pk=request.user.pk).exists()
    
    context = {
        'course': course,
        'is_enrolled': is_enrolled,
        'upload_form': ResourceForm()
    }

    if is_enrolled or request.user == course.mentor:
        context['approved_resources'] = course.resources.filter(status='Approved')
        if request.user == course.mentor:
            context['pending_resources'] = course.resources.filter(status='Pending')
            context['rejected_resources'] = course.resources.filter(status='Rejected')
            
    return render(request, 'classroom/course_detail.html', context)


@login_required
def mentor_dashboard(request):
    if not request.user.groups.filter(name='Mentors').exists():
        return redirect('classroom:student_dashboard')
        
    courses = Course.objects.filter(mentor=request.user)
    pending_resources = Resource.objects.filter(course__in=courses, status='Pending')
    
    return render(request, 'classroom/mentor_dashboard.html', {
        'courses': courses,
        'pending_resources': pending_resources
    })

@login_required
def student_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'classroom/student_dashboard.html', {'enrollments': enrollments})

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.mentor = request.user
            course.save()
            return redirect('classroom:mentor_dashboard')
    else:
        form = CourseForm()
    return render(request, 'classroom/create_course.html', {'form': form})

@login_required
def upload_resource(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.course = course
            resource.uploaded_by = request.user
            if request.user.groups.filter(name='Mentors').exists():
                resource.status = 'Approved'
            else:
                resource.status = 'Pending'
                Notification.objects.create(
                    user=course.mentor,
                    message=f"Student '{request.user.username}' submitted a new resource '{resource.title}' for your course '{course.title}'."
                )
            resource.save()
            return redirect('classroom:course_detail', course_id=course.id)
    return redirect('classroom:course_detail', course_id=course.id)

@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('classroom:course_detail', course_id=course.id)

# ... (search_results_view, approve_resource, reject_resource, notification_list views remain the same) ...
def search_results_view(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query')
    course_results = []
    resource_results = []

    if query:
        course_results = Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        resource_results = Resource.objects.filter(
            Q(title__icontains=query) & Q(status='Approved')
        )

    return render(request, 'classroom/search_results.html', {
        'form': form,
        'query': query,
        'course_results': course_results,
        'resource_results': resource_results,
    })

@login_required
def approve_resource(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    if request.user == resource.course.mentor:
        resource.status = 'Approved'
        resource.save()
        Notification.objects.create(
            user=resource.uploaded_by,
            message=f"Your resource '{resource.title}' for course '{resource.course.title}' has been approved!"
        )
    return redirect('classroom:mentor_dashboard')

@login_required
def reject_resource(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    if request.user == resource.course.mentor:
        resource.status = 'Rejected'
        resource.save()
        Notification.objects.create(
            user=resource.uploaded_by,
            message=f"Your resource '{resource.title}' for course '{resource.course.title}' has been rejected."
        )
    return redirect('classroom:mentor_dashboard')

@login_required
def notification_list(request):
    notifications = request.user.notifications.all().order_by('-created_at')
    request.user.notifications.update(is_read=True)
    return render(request, 'classroom/notifications.html', {'notifications': notifications})


# NEW view for students to delete their own resources
@login_required
def delete_resource(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    # Security check: only the user who uploaded the resource can delete it
    if request.user == resource.uploaded_by:
        resource.delete()
        messages.success(request, 'Your resource has been successfully deleted.')
    else:
        messages.error(request, 'You are not authorized to delete this resource.')
    return redirect('classroom:student_dashboard')

# NEW view for mentors to delete their own courses
@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Security check: only the mentor of the course can delete it
    if request.user == course.mentor:
        course.delete()
        messages.success(request, 'The course has been successfully deleted.')
    else:
        messages.error(request, 'You are not authorized to delete this course.')
    return redirect('classroom:mentor_dashboard')


def notifications_context_processor(request):
    if request.user.is_authenticated:
        return {'unread_notifications_count': request.user.notifications.filter(is_read=False).count()}
    return {}

