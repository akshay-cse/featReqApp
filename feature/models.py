from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS
import datetime

#Client Model
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    createdOn = models.DateField(blank=True, null=True) 

    def __str__(self):
        return self.client_name

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
    # PRIORITY_TYPES = (
    #     (HIGH, 'High'),
    #     (MEDIUM, 'Medium'),
    #     (LOW, 'Low'),
    # )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    target_date = models.DateField(blank=True, null=True)
    product_area = models.PositiveSmallIntegerField(choices=AREA_TYPES, blank=True, null=True)
    #Values from 0 to 32767 are safe in all databases supported by Django.
    feat_priority = models.PositiveIntegerField(blank=False, null=False,)
    #client List
    client = models.ForeignKey('Client',null=False, on_delete=models.CASCADE,)

    class Meta:
        unique_together = (('feat_priority', 'client',),)
    
    

 


