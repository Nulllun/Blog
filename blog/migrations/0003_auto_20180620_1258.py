# Generated by Django 2.0.6 on 2018-06-20 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20180619_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('UNKNOWN', 'unknown')], default='Unknown', max_length=1)),
                ('age', models.IntegerField()),
                ('introduction', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='bloguser',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='BlogUser',
        ),
    ]
