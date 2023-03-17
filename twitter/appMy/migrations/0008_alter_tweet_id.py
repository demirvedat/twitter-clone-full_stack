# Generated by Django 4.1.4 on 2023-03-11 13:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0007_rename_user_tweet_owner_tweet_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]