# Generated by Django 5.1 on 2024-10-11 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=450)),
                ('code', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('post_link', models.TextField()),
                ('time', models.DateField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.website')),
            ],
        ),
    ]
