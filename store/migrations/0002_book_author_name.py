# Generated by Django 4.1.6 on 2023-02-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='Author', max_length=255),
            preserve_default=False,
        ),
    ]
