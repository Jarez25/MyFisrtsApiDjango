# Generated by Django 4.2.6 on 2023-10-05 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Progamador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('ia_active', models.BooleanField(default=True)),
            ],
        ),
    ]