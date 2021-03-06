# Generated by Django 2.0.4 on 2018-04-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmdb', '0017_auto_20180424_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans', models.CharField(max_length=32)),
                ('ids', models.CharField(max_length=32)),
                ('score', models.CharField(max_length=32)),
                ('timenows', models.DateTimeField(auto_now_add=True)),
                ('ptime', models.CharField(max_length=32)),
                ('psco', models.CharField(max_length=32)),
                ('remarks', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
