from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to="Category")
    
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to="Blog")
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    user = models.CharField(max_length=255, blank = True, null =True)
    
    def __str__(self):
        return self.title