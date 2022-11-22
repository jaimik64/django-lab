from django.db import models

# Create your models here.
from django.utils import timezone
# admin, admin123 pwd
  
class State(models.Model):
    name = models.CharField(max_length = 50,unique=True)
    is_active = models.IntegerField(default = 1,
                                   blank = True,
                                    null = True,
                                    help_text ='1->Active, 0->Inactive', 
                                    choices =(
                                    (1, 'Active'), (0, 'Inactive')
                                    ))
    #created_on = models.DateTimeField(default = timezone.now,auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True, 
                                    blank = True
                                    )

                                   
    def __str__(self):
        return self.name
  
    class Meta:
        #Model Meta is basically the inner class of your model class. 
        # Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name, and a lot of other options.
        db_table = 'state'
        #We can overwrite the table name by using db_table in meta class.

        # Add verbose name
        verbose_name = 'State List'
        #verbose_name is basically a human-readable name for your model
