# Generated by Django 3.1.6 on 2021-02-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название')),
                ('anons', models.CharField(default='', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
