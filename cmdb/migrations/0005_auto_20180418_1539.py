# Generated by Django 2.0.4 on 2018-04-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20180417_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans', models.CharField(max_length=32)),
                ('ids', models.CharField(max_length=32)),
                ('score', models.CharField(max_length=32)),
                ('timenow', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Infos',
        ),
    ]
