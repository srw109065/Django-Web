# Generated by Django 4.1.10 on 2023-10-23 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_ord_mng_mdu', '0005_alter_order_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order123', to='app_ord_mng_mdu.order'),
        ),
    ]
