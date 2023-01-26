# Generated by Django 4.0.4 on 2022-07-15 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_articl_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articl',
            options={'ordering': ['-data'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AddField(
            model_name='articl',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
    ]
