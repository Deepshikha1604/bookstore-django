# Generated by Django 5.0.6 on 2024-07-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
