from django.db import models as db
from cform.models import CEntry
# Create your models here.
from sqlalchemy import func

class DEntry(db.Model):
    entry_id = db.IntegerField(primary_key=True)
    # name = db.Column(db.String(length=60), nullable=False)
    # address = db.Column(db.String(length=150), nullable=True)
    parts = db.TextField(max_length=1000, null=False)
    qty = db.IntegerField(null=False)
    price = db.IntegerField(null=False)
    time = db.DateTimeField()
    cust_id = db.ForeignKey(CEntry, on_delete=db.SET_NULL, null=True)



    def __repr__(self):
        return f"{self.entry_id} {self.parts} {self.qty} {self.price} {self.time} {self.cust_id}"
