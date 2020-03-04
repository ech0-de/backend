# Generated by Django 2.2.6 on 2019-10-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_host_api_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('properties', models.TextField()),
                ('fingerprint', models.CharField(max_length=100)),
                ('available', models.ManyToManyField(to='host.Host')),
            ],
        ),
    ]
