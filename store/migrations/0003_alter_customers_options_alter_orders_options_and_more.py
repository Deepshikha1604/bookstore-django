# Generated by Django 5.0.6 on 2024-07-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_book_author_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='uploads/book/'),
        ),
    ]