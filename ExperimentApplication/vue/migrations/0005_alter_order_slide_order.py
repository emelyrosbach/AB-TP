# Generated by Django 5.0.1 on 2024-01-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue', '0004_order_experiment_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='slide_order',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
