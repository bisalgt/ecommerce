
from django.db import models



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
    # print(dir(sub_category))
    # print('---------------')
    # print(list(sub_category.foreign_related_fields))
    # category = models.ForeignKey(Category.objects.get(id=sub_category.category.id), on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:50]
