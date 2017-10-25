from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from home import models as home_models
 
class todo(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
    
    userId = models.ForeignKey(home_models.MyProfile, on_delete=models.CASCADE)   
    name = models.CharField(max_length=30) #Like a VARCHAR field
    description = models.TextField(max_length=100) #Like a TEXT field
    date = models.DateTimeField(default=timezone.now()) #Like a DATETIME field
    completed = models.BooleanField(default=False) 

    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name