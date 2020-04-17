
from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title[:50]


class Sub_Category(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:50]



class ProductAttribute(models.Model):
    pass



class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', default='default.jpg')

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        print('models absolute url called')
        data = f"product {self.title}"
        slug = slugify(data)
        return reverse("detail_product", kwargs={"id": self.id,"slug":slug})

