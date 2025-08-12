from django.db import models

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='cars', null=True, blank=True)


    def __str__(self):
        return f"{self.name} {self.model} ({self.year}) - Kes{self.price}"
    
