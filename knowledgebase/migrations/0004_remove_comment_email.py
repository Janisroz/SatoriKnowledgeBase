# Generated by Django 4.2.7 on 2023-12-11 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0003_alter_post_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
