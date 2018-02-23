from __future__ import unicode_literals
from django.db import models
import datetime

#Client Model
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    createdOn = models.DateField(blank=True, null=True) 

# Create your models here.
class Feature(models.Model):
    POLICY = 1
    BILLING = 2
    CLAIM = 3
    REPORT =4
    AREA_TYPES = (
        (POLICY, 'Policies'),
        (BILLING, 'Billing'),
        (CLAIM, 'Claims'),
        (REPORT,'Reports'),
    )
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    PRIORITY_TYPES = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    target_date = models.DateField(blank=True, null=True)
    product_area = models.PositiveSmallIntegerField(choices=AREA_TYPES, blank=True, null=True)
    feat_priority = models.PositiveSmallIntegerField(choices=PRIORITY_TYPES, blank=True, null=True)
     # client List
    client = models.ForeignKey('Client',null=True)
    

 


