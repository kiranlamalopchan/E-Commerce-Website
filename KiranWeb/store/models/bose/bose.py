from django.db import models
from store.models.categories.subcategory import Subcategory


class Bose(models.Model):
    name = models.CharField(max_length=500)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_boselist():
        return Bose.objects.all()
