from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class extenduser(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Sex = models.CharField(max_length=50)
    Age = models.IntegerField()
    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)

class SymptomsInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField()
    pos_dis = models.TextField()