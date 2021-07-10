# Create your models here.
from django.core.files.storage import FileSystemStorage
from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    created = models.DateTimeField('date published')


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Product(models.Model):
    fs = FileSystemStorage(location='/home/david/')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(storage=fs, null=True)


class SaleProduct(models.Model):
    id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=800)


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
