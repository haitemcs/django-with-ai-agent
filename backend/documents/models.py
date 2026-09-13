from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

user = settings.AUTH_USER_MODEL # "auth.user"


#ORM
class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(default="Title")
    content = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)#DB AUTO UPDATE THE field WHEN ITS created 
    updated_at = models.DateTimeField(auto_now=True)#db auto update this field to when its updated 
