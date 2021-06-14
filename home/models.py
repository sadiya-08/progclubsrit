from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12, default='')
    email = models.CharField(max_length=122)
    subject = models.TextField(max_length=122)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name
        
class Gallery(models.Model):
    img=models.ImageField(upload_to='pics')
    doc=models.FileField(upload_to='docs', default='')
    flag=models.CharField(max_length=2, default='')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.img)
   
