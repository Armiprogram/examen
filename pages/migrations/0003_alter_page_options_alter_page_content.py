# Generated by Django 4.2.4 on 2023-09-05 14:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_pages_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['created'], 'verbose_name': 'Pagina', 'verbose_name_plural': 'Paginas'},
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
