# Generated by Django 3.2.8 on 2021-10-30 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='context',
            new_name='content',
        ),
    ]