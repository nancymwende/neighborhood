# Generated by Django 4.0.5 on 2022-06-20 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0005_neighborhood_location_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighborhood'),
        ),
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighborhood'),
        ),
    ]
