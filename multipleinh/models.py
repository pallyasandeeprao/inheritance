from django.db import models

# Create your models here.
class Bank(models.Model):#parent 1
    b_id=models.BigAutoField(primary_key=True)
    b_name=models.CharField(max_length=50)
    b_address=models.CharField(max_length=50)
class Loan(models.Model):#parent 1
    l_id = models.BigAutoField(primary_key=True)
    l_name=models.CharField(max_length=30)
    l_intrest=models.FloatField()

class Customer(Bank,Loan):#child
    c_name=models.CharField(max_length=60)
    c_email=models.EmailField()