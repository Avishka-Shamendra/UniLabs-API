# Generated by Django 3.2.6 on 2021-09-07 09:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('display_item', '0002_alter_displayitem_item_count'),
        ('lab', '0003_rename_lab_id_lab_id'),
        ('item_category', '0002_rename_item_category_itemcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('state', models.CharField(choices=[('Available', 'Available'), ('Borrowed', 'Borrowed'), ('Temp_Borrowed', 'Temp_Borrowed'), ('Damaged', 'Damaged')], default='Available', max_length=31)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('display_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display_item.displayitem')),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item_category.itemcategory')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.lab')),
            ],
        ),
    ]
