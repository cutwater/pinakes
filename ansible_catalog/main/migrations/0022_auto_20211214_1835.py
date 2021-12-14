# Generated by Django 3.2.5 on 2021-12-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0021_auto_20211214_1529"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="last_refresh_message",
            field=models.TextField(
                blank=True,
                default="",
                help_text="The message for the last source refresh",
            ),
        ),
        migrations.AddField(
            model_name="source",
            name="last_successful_refresh_at",
            field=models.DateTimeField(
                editable=False,
                help_text="The time at which the latest source refresh was succeeded",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="source",
            name="refresh_finished_at",
            field=models.DateTimeField(
                editable=False,
                help_text="The time at which the source refresh is finished",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="source",
            name="refresh_started_at",
            field=models.DateTimeField(
                editable=False,
                help_text="The time at which the source refresh is started",
                null=True,
            ),
        ),
    ]
