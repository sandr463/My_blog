# Generated by Django 2.1.5 on 2019-05-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190526_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsarticle',
            name='photo',
            field=models.ImageField(default='photo.jpg', upload_to='media'),
        ),
    ]
