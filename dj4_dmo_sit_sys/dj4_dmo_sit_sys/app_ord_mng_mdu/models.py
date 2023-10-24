from django.db import models


# Create your models here.
class Order(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    order_num = models.CharField(max_length=100)
    total_expenses = models.FloatField()
    purchase_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "app_ord_mng_mdu_order"
        ordering = ["purchase_datetime"]
        unique_together = ("username", "order_num",)


class Item(models.Model):
    order = models.ForeignKey(Order, related_name="order", on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    purchase_number = models.IntegerField()

    class Meta:
        db_table = "app_ord_mng_mdu_item"
        ordering = ["order", "-purchase_number"]
