from django.db import models

# Create your models here.
class Profile:
    userId = models.IntegerField()
    displayName = models.CharField(max_length=100)
    dateOfBirth = models.TextField()
    profileImage = models.ImageField(upload_to='profileImages')
    emailId = models.TextField()
    mobile = models.IntegerField()