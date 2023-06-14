from django.db import models as db

# Create your models here.
from sqlalchemy import func


 
class PEntry(db.Model):
    part_id = db.IntegerField(primary_key=True)
    name = db.CharField(max_length=150, null=False)
    qty = db.IntegerField(null=False)
    price = db.IntegerField(null=False)

    def __repr__(self):
        return f"{self.part_id} {self.name} {self.qty} {self.price}"