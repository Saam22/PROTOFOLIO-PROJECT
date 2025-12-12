from django.db import models

# Create your models here.
from django.utils import timezone
class Project(models.Model):
    CATEGORY_CHOICES=[
        ('web','Web Development'),
        ('mobile','Mobile Development'),
        ('design','UI/UX Design'),
        ('other','Other'),
    ]
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    description=models.TextField()
    