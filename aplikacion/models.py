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
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
                return f"{self.ingredient_name}"
    
class Product(models.Model):
    product_slug = models.SlugField(primary_key=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    product_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(upload_to="product/")
    # Lidhja many-to-one; one-to-many
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    # Lidhja many-to-many
    product_ingredient = models.ManyToManyField(Ingredient, blank=True, null=True)
    def __str__(self):
        return f"{self.product_name}"
    
class Sale(models.Model):
    # Lidhjes one-to-one
    sale_product = models.OneToOneField(Product, on_delete=models.CASCADE, blank=True, null=True)
    sale_percentage = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.sale_percentage} {self.sale_product.product_name}"
    
    @property
    def price_sale(self):
        if self.sale_percentage and self.sale_product.product_price:
            price = (self.sale_product.product_price*self.sale_percentage)/100
            new_price = self.sale_product.product_price-price
            return new_price
        else:
            return None
        
        

class Contact(models.Model):
    contact_name =models.CharField(max_length=200, null=True, blank=True)
    contact_surname =models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.contact_name} {self.contact_surname}"
    
class Book(models.Model):
    book_fullname =models.CharField(max_length=200, null=True, blank=True)
    book_email = models.EmailField(null=True, blank=True)
    book_date = models.DateField(null=True, blank=True)
    book_guests = models.PositiveSmallIntegerField(null=True, blank=True)
    book_message = models.TextField(null=True, blank=True)
    
    def __str__(self):
            return f"{self.book_fullname} {self.book_date}"