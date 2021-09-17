# Generated by Django 3.2.7 on 2021-09-17 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generos_e_tipos', '0002_auto_20210905_1224'),
        ('midias', '0002_alter_midias_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midias',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='generos_e_tipos.generos'),
        ),
        migrations.AlterField(
            model_name='midias',
            name='nota',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='midias',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='generos_e_tipos.tipos'),
        ),
    ]
