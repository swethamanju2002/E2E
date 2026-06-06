from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Service, Contact
from .models import ClientProject, StudentReview,JobApplication
from .models import Module


admin.site.register(ClientProject)
admin.site.register(StudentReview)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Service)
admin.site.register(Contact)
from django.contrib import admin
from .models import Career

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('role', 'employment_type', 'salary', 'posted_on')
    list_filter = ('employment_type',)
    search_fields = ('role',)
    
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'career', 'email', 'mobile', 'applied_on')
    search_fields = ('full_name', 'email')
    
# from .models import Course, CourseBooking


