# Generated by Django 3.2.8 on 2022-08-22 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_delete_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_complete',
            field=models.BooleanField(null=True),
        ),
    ]
