# Generated by Django 5.0.1 on 2024-02-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue', '0007_alter_order_slide_order_data_poststudy_prestudy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='confidence_score',
        ),
        migrations.RemoveField(
            model_name='data',
            name='slide_number',
        ),
        migrations.RemoveField(
            model_name='data',
            name='tcp_est',
        ),
        migrations.RemoveField(
            model_name='training',
            name='confidence_score',
        ),
        migrations.RemoveField(
            model_name='training',
            name='tcp_est',
        ),
        migrations.AddField(
            model_name='data',
            name='confidence_scores',
            field=models.CharField(default='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0', max_length=200),
        ),
        migrations.AddField(
            model_name='data',
            name='slide_numbers',
            field=models.CharField(default='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0', max_length=200),
        ),
        migrations.AddField(
            model_name='data',
            name='tcp_ests',
            field=models.CharField(default='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0', max_length=200),
        ),
        migrations.AddField(
            model_name='training',
            name='confidence_scores',
            field=models.CharField(default='0,0', max_length=200),
        ),
        migrations.AddField(
            model_name='training',
            name='slide_numbers',
            field=models.CharField(default='0,0', max_length=200),
        ),
        migrations.AddField(
            model_name='training',
            name='tcp_ests',
            field=models.CharField(default='0,0', max_length=200),
        ),
    ]