# Generated by Django 4.2.3 on 2023-07-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('expiration', models.IntegerField()),
                ('quality', models.IntegerField()),
            ],
        ),
    ]
