# Generated by Django 3.2.9 on 2021-11-28 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211126_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profildetay',
            name='job',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.jobstable'),
        ),
    ]
