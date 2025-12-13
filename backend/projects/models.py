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
    content=models.TextField(help_text="Detailed project description (supports Markdown)")
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='web')
    technologies =models.CharField(max_length=200,help_text="Comma separated list of technologies")
    image=models.ImageField(upload_to='projects/',null=True,blank=True)
    github_url =models.URLField(max_length=200,null=True,blank=True)
    live_url =models.URLField(max_length=200,null=True,blank=True)
    featured =models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =['-created_at']
    def __str__(self):
        return self.title
    
    
    class Skill(models.Model):
        name=models.CharField(max_length=100)
        level=models.IntegerField(help_text="Proficiency level from 1 to 10" ,default=1)
        category=models.CharField(max_length=100,help_text="e.g. Frontend, Backend, Design")
        icon=models.CharField(max_length=100,help_text="Icon class for frontend display",null=True,blank=True)
        order=models.IntegerField(default=0)
        
        class Meta:
            ordering =['order','name']
            
        def __str__(self):
            return self.name
        
        
    class ContactMessage(models.Model):
        name=models.CharField(max_length=100)
        email=models.EmailField()
        subject=models.CharField(max_length=200)
        message=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        read=models.BooleanField(default=False)
        
        class Meta:
            ordering =['-created_at']
            
        def __str__(self):
            return f"Message from {self.name} - {self.subject}"