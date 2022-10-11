# Generated by Django 4.1.2 on 2022-10-11 08:02

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0002_blog"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                ("title", models.CharField(max_length=200)),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        upload_to="images/gallery/", verbose_name="Image"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Gallery",},
        ),
    ]
