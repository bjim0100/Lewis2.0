# Generated by Django 3.1.6 on 2021-03-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210303_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='individual',
            field=models.BooleanField(default=False, help_text='If false, account automatically becomes a business account'),
        ),
    ]
