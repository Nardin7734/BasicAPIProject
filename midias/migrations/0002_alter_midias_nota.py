# Generated by Django 3.2.7 on 2021-09-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midias',
            name='nota',
            field=models.IntegerField(max_length=2),
        ),
    ]
