# Generated by Django 5.1 on 2024-10-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_link',
            field=models.URLField(db_index=True),
        ),
    ]
