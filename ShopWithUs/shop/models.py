from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.TextField(max_length=30)
    category = models.TextField(max_length=50, default="")
    subcategory = models.TextField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=100)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",
                              default="", blank=True, null=True)

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=70)
    email = models.TextField(max_length=70, default="")
    phone = models.TextField(max_length=70, default="")
    desc = models.TextField(max_length=100, default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.TextField(max_length=70, default='')
    name = models.TextField(max_length=70, default='')
    email = models.TextField(max_length=100, default='')
    phone = models.TextField(max_length=70, default='')
    address = models.TextField(max_length=20, default='')
    state = models.TextField(max_length=70, default='')
    city = models.TextField(max_length=70, default='')
    zip_code = models.TextField(max_length=70, default='')


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.TextField(max_length=50, default='')
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."
