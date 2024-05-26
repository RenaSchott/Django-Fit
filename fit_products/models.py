from django.db import models
from django.contrib.auth.models import User


class MainCategory(models.Model):
    """ 
    Stores a single main category
    """
    class Meta:
        verbose_name_plural = 'MainCategories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):
    """ 
    Stores a single category
    """
    class Meta:
        verbose_name_plural = 'Categories'

    main_category = models.OneToManyField(MainCategory)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """
    Stores a single product
    """
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    trainer = models.TextField(max_digits=6, decimal_places=2, null=True)
    description = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
