from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    date = models.DateField(default="2999-12-31")

# Table Header visualisation
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.mobile} {self.address} {self.date}"

