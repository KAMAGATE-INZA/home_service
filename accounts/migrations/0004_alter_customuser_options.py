# Generated by Django 5.2.1 on 2025-06-14 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['name']},
        ),
    ]
