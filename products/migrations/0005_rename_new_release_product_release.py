# Generated by Django 3.2.6 on 2021-08-23 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210823_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='new_release',
            new_name='release',
        ),
    ]