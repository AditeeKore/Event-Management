# Generated by Django 3.2.4 on 2021-06-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]