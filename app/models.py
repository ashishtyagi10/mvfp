from django.db import models

# Create your models here.


class Drug(models.Model):
    drug_name = models.CharField(max_length=200)
    available_quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(default=0.0)
    pub_date = models.DateTimeField('Date Updated')
