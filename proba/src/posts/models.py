from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=120) #karaktermező
    content=models.TextField() #szövegmező
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)

    #auto_now: mindig amikor elmenti az adatbázisba,akkor ez beállítódik arra az időpontra (True)
    #auto_now_add: csak egyszer menti el
    def __unicode__(self):  
        return self.title
    
    def __str__(self):  
        return self.title