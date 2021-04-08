# Generated by Django 2.2 on 2019-04-09 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True, verbose_name='Имя')),
                ('updated', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата обновления')),
            ],
        ),
    ]
