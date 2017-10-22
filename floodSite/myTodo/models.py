from django.db import models
from django.utils import timezone
 
class todo(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
       
    name = models.CharField(max_length=100) #Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    date = models.DateTimeField(default=timezone.now()) #Like a DATETIME field
    completed = models.BooleanField(default=False) 

    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name