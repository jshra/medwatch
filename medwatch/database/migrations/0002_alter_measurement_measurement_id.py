# Generated by Django 5.0.4 on 2024-06-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measurement_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]