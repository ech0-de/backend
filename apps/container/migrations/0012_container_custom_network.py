# Generated by Django 3.0.6 on 2020-05-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0011_container_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='custom_network',
            field=models.TextField(blank=True, null=True),
        ),
    ]
