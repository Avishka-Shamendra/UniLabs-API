# Generated by Django 3.2.6 on 2021-09-22 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_alter_requestitem_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'ordering': ('-created_at',)},
        ),
    ]
