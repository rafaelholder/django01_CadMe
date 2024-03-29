# Generated by Django 5.0.2 on 2024-03-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.TextField(max_length=255)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_birth_year', models.IntegerField()),
                ('user_course', models.TextField(max_length=128)),
            ],
        ),
    ]
