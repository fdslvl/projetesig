# Generated by Django 3.2.6 on 2021-08-21 22:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210822_0017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produit',
            options={'ordering': ('-date_added',)},
        ),
        migrations.AddField(
            model_name='produit',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]