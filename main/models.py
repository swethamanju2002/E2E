from django.db import models

# Create your models here.

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    discount=models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Module(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='modules'
    )
    module_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.module_name

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class ClientProject(models.Model):
    client_name = models.CharField(max_length=150)
    project_type = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.client_name} - {self.project_type}"


# Students Reviews Model
class StudentReview(models.Model):
    student_name = models.CharField(max_length=120)
    course_name = models.CharField(max_length=150)
    review_text = models.TextField()
    rating = models.PositiveIntegerField(default=5)  # optional: 1-5 stars
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.student_name} - {self.course_name}"
    
from django.db import models

class Career(models.Model):

    EMPLOYMENT_TYPES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    )

    role = models.CharField(max_length=200)
    job_description = models.TextField()
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES)
    salary = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='careers/', blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role
    
class JobApplication(models.Model):
    career = models.ForeignKey('Career', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    education = models.CharField(max_length=200)
    year_passed_out = models.CharField(max_length=10)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.career.role}"
    
class CourseBooking(models.Model):
    PAYMENT_CHOICES = (
        ('full', 'Full Amount'),
        ('emi', 'Installment EMI'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    education = models.CharField(max_length=200)
    year_passed = models.CharField(max_length=10)
    course = models.CharField(max_length=200)
    amount = models.IntegerField()
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ServiceBooking(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    service_name = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    preferred_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service_name}"