# Generated by Django 5.0.1 on 2024-08-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue', '0017_poststudydata_question1_poststudydata_question2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='time',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
