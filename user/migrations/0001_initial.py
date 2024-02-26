# Generated by Django 3.2.4 on 2023-09-13 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recentblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('month', models.CharField(max_length=50, null=True)),
                ('cname', models.CharField(max_length=50, null=True)),
                ('ncomm', models.CharField(max_length=1000, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/category/')),
            ],
        ),
    ]
