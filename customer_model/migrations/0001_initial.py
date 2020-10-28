# Generated by Django 3.1.2 on 2020-10-28 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=12, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('customer_id', models.IntegerField(unique=True)),
            ],
        ),
    ]