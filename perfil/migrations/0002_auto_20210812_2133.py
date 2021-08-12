# Generated by Django 3.2.6 on 2021-08-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'verbose_name_plural': 'Perfis'},
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='data_nascimento',
        ),
        migrations.AddField(
            model_name='perfil',
            name='idade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
