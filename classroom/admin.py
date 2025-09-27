from django.contrib import admin
from .models import Course, Enrollment, Resource, Notification

# This makes your models visible on the admin page.
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Resource)
admin.site.register(Notification)

