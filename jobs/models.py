from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Job(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # who posted job
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.TextField()  # simple text field for resume link/info
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"