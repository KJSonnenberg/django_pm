# Generated by Django 5.0.6 on 2024-05-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('ur', 'Urgent'), ('ac', 'Acceptable'), ('op', 'Optimized')], max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('meta_description', models.CharField(max_length=400)),
                ('content', models.TextField(blank=True, max_length=3000, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('img_src', models.CharField(blank=True, max_length=255, null=True)),
                ('img_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('img_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]