# Generated by Django 3.1.3 on 2020-12-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_signinuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangePassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_password', models.CharField(max_length=50)),
                ('new_password', models.CharField(max_length=50)),
                ('confirrm_new_password', models.CharField(max_length=50)),
            ],
        ),
    ]
