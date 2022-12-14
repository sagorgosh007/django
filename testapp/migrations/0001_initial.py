# Generated by Django 4.1.2 on 2022-10-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
