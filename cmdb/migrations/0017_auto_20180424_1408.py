# Generated by Django 2.0.4 on 2018-04-24 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0016_delete_infs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Infss',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]