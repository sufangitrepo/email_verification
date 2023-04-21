from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
from .managers import MyUserManager

class MyUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    email_verfication_token = models.CharField(max_length=200, null=True,
                                                blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = MyUserManager()
 
    def __str__(self) -> str:
        return self.email
    


@receiver(post_save,sender=MyUser)
def send_mail_for_verification(sender, instance: MyUser, created, **kwargs):
    if created:
       send_mail_verification(instance)



def send_mail_verification(instance: MyUser, ):
    uid = uuid.uuid4()
    instance.email_verfication_token = uid
    instance.save()
    subject = "email verification"
    message = f'click this link to verify your email http://127.0.0.1:8000/auth/verify/{uid}'
    receipent_list = [instance.email]
    send_mail(subject,message,settings.EMAIL_HOST_USER,receipent_list)

    
    
