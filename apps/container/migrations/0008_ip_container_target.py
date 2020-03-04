# Generated by Django 2.2.6 on 2019-10-11 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0007_container_target_status_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='container_target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='target_ip', to='container.Container'),
        ),
    ]
