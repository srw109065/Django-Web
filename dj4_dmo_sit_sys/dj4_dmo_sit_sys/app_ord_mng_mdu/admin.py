from django.contrib import admin
from .models import Order, Item


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "order_num", "username", "total_expenses", "purchase_datetime", )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "item_name", "purchase_number", )
