from django.db import models

# Create your models here.
class Service (models.Model):
    # emriVaribli = models.TipiFushen(parametra)
    service_icon = models.CharField(max_length=200, null=True, blank=True)
    service_title = models.CharField(max_length=200, null=True, blank=True)
    service_description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.service_title}"
    
class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, blank=True)
    # Slug => url
    category_slug = models.SlugField(primary_key=True)
    
    def __str__(self):
            return f"{self.category_name}"
        
class Product(models.Model):
    product_slug = models.SlugField(primary_key=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    product_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(upload_to="product/")
    # Lidhja many-to-one; one-to-many
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
                return f"{self.product_name}"
    