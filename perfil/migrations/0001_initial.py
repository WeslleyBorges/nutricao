# Generated by Django 3.2.6 on 2021-08-12 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascimento', models.DateField()),
                ('altura', models.IntegerField()),
                ('massa', models.IntegerField()),
            ],
        ),
    ]