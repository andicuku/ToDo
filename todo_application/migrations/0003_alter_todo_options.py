# Generated by Django 4.1.3 on 2022-11-04 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_application', '0002_alter_todo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'ToDo', 'verbose_name_plural': 'ToDo'},
        ),
    ]
