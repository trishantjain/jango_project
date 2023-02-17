from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=50, default="")
    head0 = models.TextField(max_length=50, default="")
    chead0 = models.TextField(max_length=50, default="")
    head1 = models.TextField(max_length=50, default="")
    chead1 = models.TextField(max_length=50, default="")
    head2 = models.TextField(max_length=50, default="")
    chead2 = models.TextField(max_length=50, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title
