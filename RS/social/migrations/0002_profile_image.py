# Generated by Django 5.0.6 on 2024-06-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to=''),
        ),
    ]