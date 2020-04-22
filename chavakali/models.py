from django.db import models
from django.contrib.auth.models import User

class Slideshows(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Mercyimageones(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")


class PrayerRequest(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField()
    prayerRequest = models.TextField()

class Events(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateTimeField()
    venue = models.CharField(max_length=250)
    speakers = models.CharField(max_length=750)

class Homemission(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Mercycover(models.Model):
    name =  models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Mercyfooter(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Mencover(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Menfooter(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Womencover(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Womenfooter(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Couplescover(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Couplesfooter(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Youthcover(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Youthfooter(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Teenscover(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Teensfooter(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Sundayschoolcover(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Sundayschoolfooter(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Wwncover(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Wwnfooter(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Bishop(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Reverend(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Eventone(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Eventtwo(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Eventthree(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Projectone(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Projecttwo(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")
    
class Projectthree(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class Drone(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")

class logo(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/%Y/%m/%d")