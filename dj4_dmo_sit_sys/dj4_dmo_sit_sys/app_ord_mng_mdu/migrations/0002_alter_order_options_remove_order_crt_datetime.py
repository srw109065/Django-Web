# Generated by Django 4.1 on 2023-09-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_ord_mng_mdu", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"ordering": ["purchase_datetime"]},
        ),
        migrations.RemoveField(
            model_name="order",
            name="crt_datetime",
        ),
    ]
