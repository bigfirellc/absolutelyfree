# Generated by Django 3.0.6 on 2020-05-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Album Name')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
