# Generated by Django 4.2.9 on 2024-02-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_alter_post_options_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(default="blog/default.jpg", upload_to="blog/"),
        ),
    ]