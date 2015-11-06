from django.db import models

from mongoengine import * 
connect('parentcoco')

class parent(Document):
	parentID = StringField()
	password = StringField()

cat = parent.objects(password="123456")
for e in cat:
	print e.parentID
