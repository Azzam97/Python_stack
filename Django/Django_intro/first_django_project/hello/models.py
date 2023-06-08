from django.db import models

# Create your models here.
class movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    director = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<movie object: {self.title} ({self.id})>"