# Generated by Django 4.2.9 on 2024-02-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created_at"]},
        ),
        migrations.RemoveField(
            model_name="comment",
            name="author",
        ),
        migrations.AddField(
            model_name="comment",
            name="name",
            field=models.CharField(default="User", max_length=255),
        ),
    ]
