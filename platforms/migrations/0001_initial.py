# Generated by Django 4.2.3 on 2023-07-14 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('UKR', 'Ukrainian'), ('ENG', 'English')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=128)),
                ('picture', models.ImageField(max_length=255, upload_to='images/')),
                ('translation', models.CharField(max_length=128)),
                ('transcription', models.CharField(blank=True, max_length=128)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platforms.language')),
            ],
        ),
    ]
