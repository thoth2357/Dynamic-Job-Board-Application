# Generated by Django 4.0.7 on 2022-10-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_alter_filter_tag_tag_search_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_tag',
            name='search_url',
            field=models.URLField(help_text="Automatically generated..Readonly Field can't be edited", null=True),
        ),
        migrations.AlterField(
            model_name='filter_tag',
            name='tag_search_category',
            field=models.CharField(default=' ', help_text='Categories to search for, separated by comma (,). Leave blank if interested in Company only.', max_length=100),
        ),
        migrations.AlterField(
            model_name='filter_tag',
            name='tag_search_company',
            field=models.CharField(default=' ', help_text='Companies name to search for', max_length=100),
        ),
        migrations.AlterField(
            model_name='filter_tag',
            name='tag_search_location',
            field=models.CharField(default=' ', help_text='Locations to search for', max_length=100),
        ),
    ]