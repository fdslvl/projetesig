from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Userprofile(models.Model):
    
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    NPA = models.CharField(max_length=255, blank=True, null=True)
    localite = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s' % self.user.username

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])
