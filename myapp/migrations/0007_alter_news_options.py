# Generated by Django 4.1 on 2022-08-24 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_category_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at']},
        ),
    ]
