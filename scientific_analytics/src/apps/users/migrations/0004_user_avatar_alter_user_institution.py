# Generated by Django 5.1.6 on 2025-03-10 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
        ('users', '0003_user_institution'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='institution.institution', verbose_name='status'),
        ),
    ]
