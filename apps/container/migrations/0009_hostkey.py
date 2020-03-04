# Generated by Django 2.2.6 on 2019-10-16 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0008_ip_container_target'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostkey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('ecdsa', 'ecdsa'), ('ed25519', 'ed25519'), ('rsa', 'rsa')], max_length=15)),
                ('public', models.TextField()),
                ('private', models.TextField(null=True)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='container.Container')),
            ],
        ),
    ]
