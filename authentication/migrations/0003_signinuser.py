# Generated by Django 3.1.3 on 2020-12-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20201220_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignInUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
