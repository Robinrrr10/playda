from django.db import models
from datetime import  datetime
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    postType = models.CharField(max_length=50)
    postedBy = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='postedImages')
    video = models.FileField(upload_to='postedVideos', null=True)
    isActive = models.BooleanField(default=True)
    postedOn = models.DateTimeField(default=now, blank=True)