# Generated by Django 4.0.7 on 2022-10-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_alter_filter_tag_search_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_tag',
            name='tag_search_category',
            field=models.CharField(blank=True, default='', help_text='Categories to search for', max_length=100, null=True),
        ),
    ]
