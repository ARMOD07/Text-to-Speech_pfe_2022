# Generated by Django 4.0.4 on 2022-05-28 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_text_dictionnaire_text_norme_alter_text_lang'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='normalization',
            new_name='transcription',
        ),
    ]
