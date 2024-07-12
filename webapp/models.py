from django.db import models

class Record(models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    order_history=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
  
def __str__(self):
    return self.first_name + ' ' + self.last_name
