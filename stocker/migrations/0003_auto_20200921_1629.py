# Generated by Django 3.1 on 2020-09-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocker', '0002_nursery_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nursery',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
