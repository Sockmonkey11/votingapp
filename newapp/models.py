from django.db import models
from django.utils import timezone
from django.conf import settings



# Create your models here.

class Question(models.Model):
    question_title = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
            self.date_created = timezone.now()
            self.save()
            
    def __str__(self):
          return self.question_title