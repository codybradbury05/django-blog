# Generated by Django 4.2.13 on 2024-06-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field_2',
            field=models.IntegerField(default=42),
        ),
    ]
