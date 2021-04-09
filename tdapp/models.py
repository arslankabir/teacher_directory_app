from django.db import models
from django.contrib.auth.models import User
from django.core import validators



# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    phone_number = models.IntegerField(null=True, blank=False)
    room_number = models.CharField(max_length=255,null=True, blank=False)
    subject_taught = models.CharField(max_length=255,null=True, blank=False)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
