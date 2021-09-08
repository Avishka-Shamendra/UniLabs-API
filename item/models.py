from django.db import models
from uuid import uuid4

from display_item.models import DisplayItem
from lab.models import Lab
from item_category.models import ItemCategory
from django.utils.translation import gettext_lazy as _
from django.db.models.deletion import CASCADE

#State field options for item
class State(models.TextChoices):
    AVAILABLE='Available', _('Available')
    BORROWED='Borrowed', _('Borrowed')
    TEMP_BORROWED='Temp_Borrowed', _('Temp_Borrowed')
    DAMAGED='Damaged', _('Damaged')

#Item Model

class Item(models.Model):
    id=models.UUIDField(default=uuid4,primary_key=True,editable=False)
    display_item=models.ForeignKey(DisplayItem,on_delete=CASCADE)
    item_category=models.ForeignKey(ItemCategory,on_delete=CASCADE)
    lab=models.ForeignKey(Lab,on_delete=CASCADE)
    state=models.CharField(max_length=31,choices=State.choices,default='Available')
    added_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'id'   
