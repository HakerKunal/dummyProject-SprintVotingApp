# Generated by Django 4.0.4 on 2022-05-12 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='start_date',
            field=models.DateField(),
        ),
    ]
