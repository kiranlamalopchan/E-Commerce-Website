# Generated by Django 3.1.7 on 2021-03-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_auto_20210302_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory',
            field=models.CharField(blank=True, default=1, max_length=500, null=True),
        ),
    ]