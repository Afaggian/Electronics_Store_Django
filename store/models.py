from django.db import models
from django.urls import reverse


# class related to the products for sale
class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    image = models.ImageField(default='')
    description = models.TextField(default="", blank=True)

#Class to give attributes to our father class, in this case will order the products per price
    # and not allow to give the products a negative price
    class Meta:
        ordering = ['price']
        constraints = [
            models.CheckConstraint(check=models.Q(price__gte=0), name="price_not_negative")
        ]

#method to add a link to the url of the product at the admin page
    def get_absolute_url(self):
        return reverse("store:product-detail", kwargs={"pk": self.id})


#function to show the name of the product on my list of products at the admin interface
    def __str__(self):
        return f"{self.name}, ${self.price}"
