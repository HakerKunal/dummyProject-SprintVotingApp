# Generated by Django 4.0.4 on 2022-05-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0002_sprint_is_active_alter_sprint_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=35, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='sprint',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
