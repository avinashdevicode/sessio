from django.db import models
from django.core.files.storage import FileSystemStorage
from time import time

def upload_file_name(instance, filename):
    return 'upload/%s_%s' % (str(time() ).replace('.','_'), filename)
# Create your models here.

class products(models.Model):
    product_name = models.CharField(max_length = 60)
    product_description = models.TextField()
    added_on = models.DateTimeField(auto_now_add = True)
    product_photo = models.FileField(upload_to = upload_file_name)
    
    def __unicode(self):
        return self.product_name