# Generated by Django 3.2.6 on 2021-08-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0004_auto_20210826_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='statut',
            field=models.CharField(choices=[('commande', 'Commande'), ('livre', 'Livre'), ('arrive', 'Arrive')], default='commande', max_length=20),
        ),
    ]