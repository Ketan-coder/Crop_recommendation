# Generated by Django 4.1.6 on 2024-01-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0002_alter_croprecommendation_humidity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='croprecommendation',
            name='label',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]