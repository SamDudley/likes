# Generated by Django 3.0.7 on 2020-06-06 12:40

from django.db import migrations


def initial_post(apps, schema_editor):
    Post = apps.get_model("likes", "Post")

    Post.objects.create(content="This is the first post and it's wonderful.")


class Migration(migrations.Migration):

    dependencies = [
        ("likes", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(initial_post),
    ]