from django import template
from classroom.models import Enrollment

register = template.Library()

@register.filter(name='get_enrollment_status')
def get_enrollment_status(course, user):
    """
    Custom template filter to check if a user is enrolled in a course.
    Usage in template: {{ course|get_enrollment_status:user }}
    """
    if user.is_authenticated:
        return Enrollment.objects.filter(course=course, student=user).exists()
    return False
