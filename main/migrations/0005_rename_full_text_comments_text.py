# Generated by Django 4.0.4 on 2023-01-16 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='full_text',
            new_name='text',
        ),
    ]
