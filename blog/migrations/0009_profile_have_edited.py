# Generated by Django 2.0.6 on 2018-06-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180620_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='have_edited',
            field=models.BooleanField(default=False),
        ),
    ]