from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.contrib.auth.models import User
from django.utils.timezone import now

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title =models.CharField(max_length=50,default="")
    head0 = models.CharField(max_length=500,default='')
    chead0 = models.CharField(max_length=50000,default='')
    head1 = models.CharField(max_length=500,default='')
    chead1 = models.CharField(max_length=50000,default='')
    head2 = models.CharField(max_length=500,default='')
    chead2 = models.CharField(max_length=50000,default='')
    pub_date = DateField()
    thumbnail =models.ImageField(upload_to="shop/images")

    def __str__(self):
        return self.title