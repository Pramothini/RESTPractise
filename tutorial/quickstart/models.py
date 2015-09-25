from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class List(models.Model): 
	user = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now_add=True)
	listname = models.CharField(max_length=40)
    
        def email(self):
            return self.user.email
	def __unicode__(self):
           return 'id=' + str(self.id) +'('+self.user.username+')'
