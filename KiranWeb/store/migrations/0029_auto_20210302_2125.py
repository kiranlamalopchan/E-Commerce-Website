# Generated by Django 3.1.7 on 2021-03-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20210302_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
