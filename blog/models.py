from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=30)
    
    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField( null=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return  self.full_name()
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt= models.TextField()
    image_name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False)
    slug = models.SlugField(unique=True)
    content = models.TextField(MinLengthValidator(10) )
    caption = models.ManyToManyField(Tag, null=True, blank=True)
    author = models.ForeignKey(Author,null=True, on_delete=models.SET_NULL, related_name="posts")
    
    def __str__(self):
        return self.title