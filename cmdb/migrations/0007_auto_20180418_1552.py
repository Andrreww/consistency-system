# Generated by Django 2.0.4 on 2018-04-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20180418_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans', models.CharField(max_length=32)),
                ('ids', models.CharField(max_length=32)),
                ('score', models.CharField(max_length=32)),
                ('timenow', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Info1',
        ),
    ]