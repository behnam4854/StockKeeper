from django.db import models

# Create your models here.
class Category(models.Model):
    """making easier to catogrize the product"""
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    cat = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    

# Category
