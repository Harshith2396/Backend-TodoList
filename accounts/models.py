from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 

class userManagerAccounts(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("email needs to be specified")
        user=self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_staffuser(self,email,password):
        user=self.create_user(email,password=password)
        user.staff=True
        user.save(using=self.db)
        return user
    def create_superuser(self,email,password):
        user=self.create_user(email,password=password)
        user.staff=True
        user.save(using=self.db)
        return user
    def create_users(self,email,password):
        user=self.create_user(email,password=password)
        user.save(using=self.db)
        return user
class UserAccounts(AbstractBaseUser):
    email=models.CharField(primary_key=True,max_length=155)
    username=models.CharField(max_length=150)
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    time_stamp=models.DateTimeField(auto_now=True)
    USERNAME_FIELD='email'
    REQUIRED_FILED=[]
    def get_username(self):
        return self.username
    def get_first_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    objects=userManagerAccounts()