# Generated by Django 4.1.7 on 2023-02-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]