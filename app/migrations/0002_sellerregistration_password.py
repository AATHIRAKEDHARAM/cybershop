# Generated by Django 4.0.3 on 2022-06-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerregistration',
            name='password',
            field=models.CharField(default=10, max_length=120),
            preserve_default=False,
        ),
    ]
