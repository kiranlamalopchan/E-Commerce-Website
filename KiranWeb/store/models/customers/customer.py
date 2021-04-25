from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    email = models.EmailField(max_length=50)
    mobilenumber = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.IntegerField()
    check = models.CharField(max_length=15, default="Not Choosen")

    def __str__(self):
        return self.username

    def usernamevalidation(self):
        if Customer.objects.filter(username=self.username):
            return True
        return False

    def signupcustomer(self):
        self.save()

    @staticmethod
    def get_customer_forlogin(username):
        try:
            return Customer.objects.get(username=username)
        except:
            return False
