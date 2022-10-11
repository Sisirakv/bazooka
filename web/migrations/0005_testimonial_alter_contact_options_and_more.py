# Generated by Django 4.1.2 on 2022-10-11 10:27

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0004_servicecategory_service"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
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
                        upload_to="images/testimonial/", verbose_name="Image"
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("review", models.TextField()),
            ],
            options={"verbose_name_plural": "Testimonial",},
        ),
        migrations.AlterModelOptions(
            name="contact", options={"verbose_name_plural": "Contact"},
        ),
        migrations.AlterModelOptions(
            name="service", options={"verbose_name_plural": "Service"},
        ),
    ]
