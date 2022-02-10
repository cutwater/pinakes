# Generated by Django 3.2.5 on 2022-02-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0034_source_info"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="last_refresh_task_ref",
            field=models.CharField(
                help_text="The last refresh task id", max_length=64, null=True
            ),
        ),
    ]
