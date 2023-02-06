from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",
                              default="", blank=True, null=True)

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=700, default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=70, default='')
    name = models.CharField(max_length=70, default='')
    email = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=70, default='')
    address = models.CharField(max_length=200, default='')
    state = models.CharField(max_length=70, default='')
    city = models.CharField(max_length=70, default='')
    zip_code = models.CharField(max_length=70, default='')


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(max_length=100, default='')
    update_desc = models.CharField(max_length=5000, default='')
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."
