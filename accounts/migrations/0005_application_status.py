# Generated by Django 3.1.4 on 2020-12-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201224_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected'), ('completed', 'completed')], default='pending', max_length=100, null=True),
        ),
    ]
