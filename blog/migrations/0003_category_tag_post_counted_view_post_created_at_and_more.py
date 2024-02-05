# Generated by Django 4.2.9 on 2024-02-04 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="counted_view",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="published_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="post",
            name="status",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
