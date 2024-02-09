from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Sneakers(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    character = models.TextField()
    UZ = "so'm"
    RU = "₽"
    USD = "$"
    the_prise = (
        (UZ, "so'm"),
        (RU, "₽"),
        (USD, "$")
    )
    price_type = models.CharField(max_length=10, choices=the_prise, default='so\'m')
    price = models.IntegerField()
    image = models.ImageField()
    def __str__(self):
        return self.name

class Buy(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Sneakers, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=255)
    ALL_SIZES = (
        ("36", "36"),
        ("37", "37"),
        ("38", "38"),
        ("39", "39"),
        ("40", "40"),
        ("41", "41"),
        ("42", "42"),
        ("43", "43"),
        ("44", "44"),

    )
    size = models.CharField(max_length=255, choices=ALL_SIZES)
    ALL_VALUS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    how = models.CharField(max_length=255, choices=ALL_VALUS)
    map = models.TextField()
    email = models.EmailField(blank=True)
    def __str__(self):
        return self.name
class Advertising(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    subtitle = models.CharField(max_length=255)


class Register(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    message = models.TextField()
    def __str__(self):
        return self.name