# Generated by Django 3.1.6 on 2021-02-23 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210223_2045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='full_text',
            new_name='text',
        ),
    ]
