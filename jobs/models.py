from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#Category model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name



class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs',default=1)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deadline = models.DateField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


def upload_to(instance, filename):
    return f"applications/{instance.job.id}/{filename}"

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Only if users must be logged in
    cv = models.FileField(upload_to=upload_to)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application by {self.user.email} for {self.job.title}"


