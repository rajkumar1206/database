# Generated by Django 3.1.3 on 2020-11-18 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='nationality',
            field=models.CharField(default='India', max_length=10),
        ),
    ]
