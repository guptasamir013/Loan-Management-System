# Generated by Django 3.1.4 on 2020-12-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='dependents',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='income',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='married',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='property_area',
            field=models.CharField(blank=True, choices=[('rural', 'rural'), ('urban', 'urban'), ('semiurban', 'semiurban')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='self_employed',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='education',
            field=models.CharField(blank=True, choices=[('graduate', 'graduate'), ('not graduate', 'not graduate')], max_length=100, null=True),
        ),
    ]
