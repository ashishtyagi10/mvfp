from django.db import models
from django.conf import settings
from django.shortcuts import reverse
# https://medium.com/analytics-vidhya/how-to-create-simple-e-commerce-website-with-django-step-1-of-5-42c6cca414c2
# https://medium.com/analytics-vidhya/how-to-create-fully-functional-e-commerce-website-with-django-c95b46973b0
# https://medium.com/analytics-vidhya/how-to-create-fully-functional-e-commerce-website-with-django-997ffaa0f040
# https://medium.com/analytics-vidhya/how-to-create-fully-functional-e-commerce-website-with-django-7205d250e76f
# https://medium.com/analytics-vidhya/how-to-create-a-fully-functional-e-commerce-website-with-django-d4b998bac01

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()+self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self) -> str:
        return super().__str__()+self.name

    def get_absolute_url(self):
        return reverse("app:product", kwargs={"pk": self.pk})

    def get_add_to_cart_url(self):
        return reverse("app:add-to-cart", kwargs={"pk": self.pk})

    def get_remove_from_cart_url(self):
        return reverse("app:remove-from-cart", kwargs={
            "pk": self.pk
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
