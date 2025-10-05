from django import template
from classroom.models import Enrollment

register = template.Library()

@register.filter(name='get_enrollment_status')
def get_enrollment_status(course, user):
    """
    Checks if a user is enrolled in a specific course.
    Usage: {{ course|get_enrollment_status:user }}
    """
    if user.is_authenticated:
        return Enrollment.objects.filter(course=course, student=user).exists()
    return False

# NEW filter to get a user's role
@register.filter(name='get_user_role')
def get_user_role(user):
    """
    Returns the user's role ('Mentor' or 'Student').
    Usage: {{ user|get_user_role }}
    """
    if user.groups.filter(name='Mentors').exists():
        return 'Mentor'
    return 'Student'

