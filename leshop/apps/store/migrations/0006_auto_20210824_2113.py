# Generated by Django 3.2.6 on 2021-08-24 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_produit_vedette'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='produit',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
