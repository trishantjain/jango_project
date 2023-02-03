# Generated by Django 4.1.2 on 2023-01-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_alter_product_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("msg_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=70)),
                ("email", models.CharField(default="", max_length=70)),
                ("phone", models.CharField(default="", max_length=70)),
                ("desc", models.CharField(default="", max_length=700)),
            ],
        ),
    ]
