# Generated by Django 2.0.4 on 2018-04-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(max_length=32)),
                ('score', models.CharField(max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='Userinfo',
        ),
    ]
