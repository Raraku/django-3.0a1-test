from django.db import models
import datetime
from django.utils.timezone import make_aware
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Goattime(models.Model):
    time_uploaded = models.DateTimeField()
    
    def __str__(self):
        return str(self.time_uploaded)

    def save(self, *args, **kwargs):
        raw_date = datetime.datetime.fromtimestamp(1440455313.0)
        raw_date = raw_date.replace(minute=0, hour=0, second=0)
        self.time_uploaded=make_aware(raw_date)
        super(Goattime, self).save(*args, **kwargs)

class Goatlist(models.Model):
    list = JSONField(blank=True, null=True)

    def __str__(self):
        
        return 
