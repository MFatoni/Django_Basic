from django.db import models

class Dreamreal(models.Model):
	website = models.CharField(max_length=50)
	mail = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	phonenumber = models.IntegerField()

	class Meta:
		db_table = "dreamreal"

class Profile(models.Model):
	name = models.CharField(max_length=50)
	picture = models.ImageField(upload_to='picture')

	class Meta:
		db_table = "profile"