from django.db import models

# Create your models here.

class Post(models.Model):
    postType = models.CharField(max_length=50)
    postedBy = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='postedImages')
    isActive = models.BooleanField(default=True)