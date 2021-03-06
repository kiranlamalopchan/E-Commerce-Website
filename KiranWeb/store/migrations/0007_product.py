# Generated by Django 3.1.7 on 2021-02-28 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('keyword', models.CharField(max_length=1000)),
                ('specs', models.CharField(default=None, max_length=5000000)),
                ('description', models.CharField(max_length=5000)),
                ('price', models.IntegerField(default='Comming Soon', max_length=200)),
                ('image', models.ImageField(upload_to='uploads/product/other/')),
                ('category', models.ForeignKey(default=7, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]
