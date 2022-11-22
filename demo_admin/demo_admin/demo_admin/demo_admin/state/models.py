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
                                    #Extra “help” text to be displayed with the form widget
                                    choices =(
                                    (1, 'Active'), (0, 'Inactive')
                                    ))
    created_on = models.DateTimeField(auto_now_add=True)
    # auto_now_add:- Automatically set the field to now when the object is first created. Useful for creation of timestamps. 
    # Note that the current date is always used
    updated_on = models.DateTimeField(default = timezone.now,
    # default:- The default value for the field. 
    # timezone.now:- The default time zone is 
    # the time zone defined by the TIME_ZONE in setting.py
                                   null = True, 
                                  blank = True, verbose_name = "updatedon"
                                 )

                                   
    def __str__(self):
        return self.name
        # By default the Django admin site displays model objects as a simple list with the 
        # string representation of the model object as title. 
        # If no _str_ method provided, then Django uses the models name as the title. We can fix this 
        # by adding a __str__method to our model. 
  
    class Meta:
        # inner class of model class.
        # used to change the behavior of your 
        # model fields like changing order options,verbose_name etc
        db_table = 'state'
        # for overwriting table name

        # Add verbose name
        verbose_name = 'StateList'
        # A human-readable name for the field. 
        # If the verbose name isn’t given, 
        # Django will automatically create 
        # it using the field’s attribute name, 
        # converting underscores to spaces.

