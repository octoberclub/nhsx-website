# Generated by Django 3.0.4 on 2020-04-06 11:00

from django.conf import settings
from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_posts', '0005_auto_20200403_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='pages_blogpost', to=settings.AUTH_USER_MODEL),
        ),
    ]
