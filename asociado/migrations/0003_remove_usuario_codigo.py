# Generated by Django 3.2.8 on 2023-07-09 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asociado', '0002_usuario_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='codigo',
        ),
    ]
