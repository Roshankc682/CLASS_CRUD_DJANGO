from django.db import models
from django.urls import reverse
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10000)

    def get_absolute_url(self):
        return reverse("books:books-single", kwargs={"id": self.id})
    