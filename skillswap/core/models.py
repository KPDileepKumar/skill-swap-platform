from django.db import models

from django.contrib.auth.models import User
import uuid



# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    username=models.CharField(max_length=200,null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    PROFILE_TYPE=(('public','Public'),('private','Private'))
    AVAILABLE_OPTIONS=(('weekday','WeekDays'),('weekend','WeekEnds'),('evening','Evenings'))
    available=models.TextField(choices=AVAILABLE_OPTIONS,max_length=200)
    profile=models.TextField(choices=PROFILE_TYPE,max_length=200)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    def __str__(self):
        return str(self.username)
    
class OfferedSkill(models.Model):
    owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    def __str__(self):
        return self.name

class RequestedSkill(models.Model):
    owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    def __str__(self):
        return self.name
    

class Requests(models.Model):
    sender=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name='sender_requests')
    recipient=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name='recipient_requests')
    message=models.TextField()
    STATUS_CHOICES = (
            ('pending', 'Pending'),
            ('accept', 'Accept'),
            ('reject', 'Reject'),
        )

    status = models.CharField(
            max_length=10,
            choices=STATUS_CHOICES,
            default='pending'
        )
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    def __str__(self):
        return f"{self.sender}-->{self.recipient}"
