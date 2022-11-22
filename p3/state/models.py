from email.policy import default
from secrets import choice
from django.db import models

# Create your models here.
from django.utils import timezone

class State(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.IntegerField(
        default = 1,
        blank = True,
        null = True,
        help_text='1->active, 0->inactive',
        choices =((1, 'active'), (0,'inactive'))
    )
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(
        default=timezone.now,
        null =False,
        # blank=False,
        verbose_name="updatedon"
    )

    class Meta:
        db_table="state"
        verbose_name = "StateLists"
    # db_table = "new State"