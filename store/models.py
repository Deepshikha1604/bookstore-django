from django.db import models
import datetime


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=250)
    author_name = models.CharField(max_length=250,default='')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=1)
    UnitPrice = models.DecimalField(max_digits=10,decimal_places=2)
    UnitsinStock = models.SmallIntegerField()
    image = models.ImageField(upload_to='products/')

    
    def __str__(self):
        return self.name


class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = 'Customers'


class Orders(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100,default='',blank=False)
    phone = models.CharField(max_length=10,default='',blank=False)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Orders'