# Generated by Django 4.0.4 on 2022-04-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='house_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]