# Generated by Django 5.1 on 2024-09-01 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_at',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='text',
        ),
    ]
