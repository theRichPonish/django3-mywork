# Generated by Django 3.1.3 on 2020-12-21 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_changepassword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='changepassword',
            old_name='confirrm_new_password',
            new_name='confirm_new_password',
        ),
    ]
