# Generated by Django 4.1.1 on 2022-11-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_remove_goodsbooks_img_goodsbooks_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsbooks',
            name='name',
            field=models.CharField(default='null', max_length=40, verbose_name='Name'),
        ),
    ]
