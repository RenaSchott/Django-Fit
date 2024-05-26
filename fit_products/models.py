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

    main_category = models.ManyToManyField(MainCategory)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
