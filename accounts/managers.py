from django.contrib.auth.models import BaseUserManager
# from .models import MyUser

class MyUserManager(BaseUserManager):


    def create(self, email, password,**kwargs):
        if not email:
            raise ValueError('email is required')
        elif not password:
            raise ValueError('password is required')
        
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email, password, **kwargs):
        user = self.create(email=email, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

