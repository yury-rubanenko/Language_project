# Generated by Django 4.2.5 on 2023-09-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("platforms", "0012_alter_tag_name_alter_word_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="HttpRequestLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("method", models.CharField(max_length=10)),
                ("path", models.CharField(max_length=255)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
