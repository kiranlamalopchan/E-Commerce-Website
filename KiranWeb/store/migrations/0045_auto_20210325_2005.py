# Generated by Django 3.1.7 on 2021-03-25 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_order_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.ForeignKey(blank=True, default='', max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]
