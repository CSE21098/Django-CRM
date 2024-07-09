from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    zipcode = models.CharField(max_length=6)

    def __str__(self):
        return self.name


