# Generated by Django 4.0.4 on 2022-05-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='project',
            name='source_code',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]