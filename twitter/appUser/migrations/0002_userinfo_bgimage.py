# Generated by Django 4.1.4 on 2023-03-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='bgimage',
            field=models.FileField(blank=True, default='default.profil', upload_to=''),
        ),
    ]
