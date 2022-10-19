from django.db import models

# Create your models here.
class Coffee(models.Model):
	name = models.CharField(max_length = 20) 
	bean_from = models.CharField(max_length = 10) 
	price = models.DecimalField(max_digits = 3, decimal_places=0) # 3 digits, 0 decimal places