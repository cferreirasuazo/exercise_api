from django.db import models

# Create your models here.


# auto_now_add is perfect for a one-off modification of a field on your model, ONLY when the model instance is created and saved for the first time. As you noted, it is great for a created_at or timestamp field will never need to change again.

# auto_now is awesome for whenever you need a field to change anytime the .save() method is called on the model instance. updated_at would be a great opportunity for this, as you mentioned.

class Log(models.Model):
    description = models.TextField()
    duration = models.IntegerField()
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"{self.description} - {self.date}"
