# -*- coding: UTF-8 -*-
from django.db import models

#import User
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.


class DatePost(models.Model):
    DepOptions = (
        ("RD", "RD"),
        ("RDI", "RDI"),
        ("RDII", "RDII"),
    )

    TimeOptions = (
        ("True","上午"),
        ("False","下午"),
    )

    author = models.ForeignKey(User)
    title = models.CharField(max_length=200,editable = False)
    dep = models.CharField(max_length=100,choices = DepOptions,default = True)
    leaveDate = models.DateField(blank=True, null=True)
    timeRange = models.CharField(max_length=100,choices = TimeOptions)
    created_date = models.DateTimeField(default=timezone.now,editable = False)
    is_check = models.BooleanField(default = False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        self.title = "[%s] %s - %s" % (self.leaveDate,self.dep, self.author)
        super(DatePost, self).save(*args, **kwargs)