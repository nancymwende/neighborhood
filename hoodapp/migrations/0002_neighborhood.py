# Generated by Django 4.0.5 on 2022-06-19 08:45

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hoodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighborHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('content', models.TextField(max_length=600, null=True)),
                ('occupants_count', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('health_cell', models.IntegerField(blank=True, null=True)),
                ('police_hotline', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
