from django.db import models
from file.models import File


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
