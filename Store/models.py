from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=128)
    productPrice = models.DecimalField(decimal_places=2, max_digits=10)
    productImageLink = models.URLField()
    productLink = models.URLField()

    def __str__(self):
        return self.productName + " Cost: £" + str(self.productPrice)

