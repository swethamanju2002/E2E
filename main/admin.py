from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Service, ServiceDemoLink, Contact
from .models import ClientProject, StudentReview,JobApplication
from .models import WorkshopPhoto, Certificate
from .models import Module
from .models import Internship

from .models import UpcomingWorkshop
from .models import DemoCategory, DemoRequest




admin.site.register(ClientProject)
admin.site.register(StudentReview)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(UpcomingWorkshop)

class ServiceDemoLinkInline(admin.TabularInline):
    model = ServiceDemoLink
    extra = 1
 
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [ServiceDemoLinkInline]
 

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

@admin.register(WorkshopPhoto)
class WorkshopPhotoAdmin(admin.ModelAdmin):
    list_display  = ('title', 'event_date', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    list_filter   = ('event_date',)
    ordering      = ('order', '-created_at')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display  = ('course_name', 'cert_type', 'order', 'created_at')
    list_editable = ('order',)
    list_filter   = ('cert_type',)
    search_fields = ('course_name',)
    ordering      = ('order', '-created_at')

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'price', 'duration')
  
    search_fields = ('title',)
    
@admin.register(DemoCategory)
class DemoCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "demo_link", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(DemoRequest)
class DemoRequestAdmin(admin.ModelAdmin):
    list_display = (
        "organization_name",
        "email",
        "mobile",
        "category",
        "status",
        "created_at",
    )

    list_filter = ("status", "category")
    search_fields = (
        "organization_name",
        "email",
        "mobile",
        "custom_requirement",
    )

    readonly_fields = ("created_at",)