"""
User model.

Represents a registered user in the system.
Used for authentication and authorization.
"""
from django.db import models
# Create your models here.

class Collection(models.Model):
    """ Type 
    + means we dont care about the reverce relationship"""
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null = True,
        related_name='+'
    )

class Promotion(models.Model):
    """Promotion data"""
    description = models.CharField(max_length=255)
    # product_set
    discount = models.FloatField()


class Product(models.Model):
    """ A product which is related to collection .
    what kind of product it is .
    if we delete a collection , we dont delete the product . 
    because a single product can be in many collections"""
    # sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255) #varchar(255)
    slug = models.SlugField()
    description = models.TextField()
    # max price = 9999.99
    unit_price = models.DecimalField(max_digits=6 , decimal_places= 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    """Data about the customer
    Account detais"""
    MEMBERSHIP_BRONZE ='B'
    MEMBERSHIP_SILVER ='S'
    MEMBERSHIP_GOLD ='G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1 ,
        choices= MEMBERSHIP_CHOICES ,
        default=MEMBERSHIP_BRONZE
    )


class Order(models.Model):
    """orders related to the customers
    we dont delete the orders when a customer is deleted 
    because its the sales."""
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING ,'Pending'),
        (PAYMENT_STATUS_COMPLETE , 'Complete'),
        (PAYMENT_STATUS_FAILED ,'Failed')
    ]
    placed_at =models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default= PAYMENT_STATUS_PENDING
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    """order = which order it belongs to
     product = which product it is  
     """
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    """
    Address of the customers"""
    street = models.CharField(max_length= 255)
    city = models.CharField(max_length= 255)
    # one to one
    # customor = models.OneToOneField(Customor,on_delete=models.CASCADE,primary_key=True)
    #One to Many
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)


class Cart(models.Model):
    """The cart """
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    """Items in the cart
    cart = which cart it belongs to
    product = which product it is """

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
