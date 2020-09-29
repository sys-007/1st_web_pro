from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional field 1
    portfolio_site = models.URLField(blank=True)

    # additional field 2
    # pip install pillow to use this!
    profile_pic = models.ImageField(upload_to='profile_pic',
                                    blank=True)

    # string representation
    def __str__(self):
        return self.user.username