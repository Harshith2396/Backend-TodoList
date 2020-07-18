from django.db import models
from accounts.models import UserAccounts
class tasks(models.Model):
    task=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    task_id=models.AutoField(primary_key=True)
    email=models.ForeignKey(UserAccounts,on_delete=models.CASCADE)
class user_password_reset_time(models.Model):
    '''
    THIS MODEL IS USED TO TRACK THE USER'S ACTIVITY ON THE PASSWORD RESET LINK.
    The user will be able to send password reset link once every 5 mins only,
    the time can be changed in user_expiration.py file 
    '''
    user=models.CharField(max_length=155,primary_key=True)
    time=models.DateTimeField(auto_now=True)