# Generated by Django 3.1.7 on 2021-02-28 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banners_category',
            field=models.ForeignKey(default=7, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcategory'),
        ),
    ]
