# Generated by Django 4.2.3 on 2023-08-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0008_alter_word_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('ua', 'Ukrainian')], max_length=2),
        ),
    ]