# Generated by Django 5.1 on 2024-08-31 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineorder', '0005_alter_add_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemadd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverytime', models.TextField()),
                ('deliveryaddress', models.TextField(max_length=200)),
                ('phonenumber', models.TextField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineorder.menu')),
            ],
        ),
    ]
