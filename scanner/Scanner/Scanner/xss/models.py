from django.db import models

# Create your models here.
class Domain(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.domain

class Xss(models.Model):
    Xssid = models.ForeignKey(Domain, on_delete=models.PROTECT)
    xssurl = models.CharField(max_length=500)


    def __str__(self):
        return self.xssurl

class Lfi(models.Model):
    Lfiid = models.ForeignKey(Domain, on_delete=models.PROTECT)
    lfiurl = models.CharField(max_length=500)


    def __str__(self):
        return self.lfiurl

class Redirect(models.Model):
    Redirectid = models.ForeignKey(Domain, on_delete=models.PROTECT)
    redirecturl = models.CharField(max_length=500)


    def __str__(self):
        return self.redirecturl

class SubdomainTakeover(models.Model):
    Stid = models.ForeignKey(Domain, on_delete=models.PROTECT)
    Sturl = models.CharField(max_length=500)
    
class Xsspayload(models.Model):
    payload = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.payload

class Lfipayload(models.Model):
    payload = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.payload


class Hstpayload(models.Model):
    payload = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.payload

