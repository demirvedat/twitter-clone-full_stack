# Generated by Django 4.1.4 on 2023-03-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0007_alter_userinfo_bgimage_alter_userinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='bgimage',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]