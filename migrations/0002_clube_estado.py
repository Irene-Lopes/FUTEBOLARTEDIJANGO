# Generated by Django 5.0.2 on 2024-02-21 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clube',
            name='estado',
            field=models.CharField(choices=[('AC', 'Acre'), ('RS', 'Rio Grande do Sul'), ('SP', 'São Paulo')], max_length=120, null=True),
        ),
    ]
