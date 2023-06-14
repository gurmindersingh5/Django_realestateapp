from django.db import models as db

from sqlalchemy import func


class CEntry(db.Model):
    cust_id = db.IntegerField(primary_key=True)
    name = db.CharField(max_length=60, null=False)
    address = db.TextField(max_length=200, null=True)
    contact = db.CharField(max_length=10, null=True)

    def __repr__(self):
        return f"{self.name} {self.address} {self.contact}"

