from django.db import models

# Create your models here.
class Bank(models.Model):#parent
    b_name=models.CharField(max_length=50)
    b_ifsc=models.IntegerField()
    b_addres=models.CharField(max_length=50)
    def __str__(self):
        return self.b_name

class Loan(Bank):#intermidate
    l_name=models.CharField(max_length=50)
    rateofintrest=models.FloatField()
    duration=models.CharField(max_length=50)
    def __str__(self):
        return self.l_name

class User(Loan):#child
    u_name=models.CharField(max_length=60)
    u_mobile=models.BigIntegerField()
    u_email=models.EmailField()
    def __str__(self):
        return self.u_name