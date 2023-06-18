from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, PostData):
        errors = {}
        if len(PostData['name']) < 5:
            errors['name'] = "Name should be at least 5 characters long"
        if len(PostData['desc']) < 15:
            errors['desc'] = "Description should be at least 15 characters long"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return f"course: {self.name}"


class Description(models.Model):
    desc = models.CharField(max_length=255)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.desc}"