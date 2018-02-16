from __future__ import unicode_literals
from django.db import models

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
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    # client List
    # client priority
    target_date = models.DateField(blank=True, null=True)
    product_area = models.PositiveSmallIntegerField(choices=AREA_TYPES, blank=True, null=True)

