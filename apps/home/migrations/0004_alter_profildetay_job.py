# Generated by Django 3.2.9 on 2021-11-28 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_profildetay_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profildetay',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.jobstable'),
        ),
    ]