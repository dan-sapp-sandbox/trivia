# Generated by Django 5.1.3 on 2024-11-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('types', models.TextField()),
                ('gen_of_first_appearance', models.TextField()),
            ],
        ),
    ]