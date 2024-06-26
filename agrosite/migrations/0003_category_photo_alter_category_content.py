# Generated by Django 4.2.11 on 2024-04-02 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrosite', '0002_alter_category_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='category',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
