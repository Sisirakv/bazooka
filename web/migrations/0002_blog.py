# Generated by Django 4.1.2 on 2022-10-11 07:23

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        upload_to="images/blog/", verbose_name="Image"
                    ),
                ),
                ("heading", models.TextField()),
                ("date", models.DateField(auto_now_add=True)),
                ("content", models.TextField()),
            ],
            options={"verbose_name_plural": "Blog",},
        ),
    ]