# Generated by Django 3.1.5 on 2023-06-21 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200)),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='places/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='places', to='volunteer.region')),
            ],
            options={
                'ordering': ['-region'],
                'index_together': {('id', 'slug')},
            },
        ),
    ]
