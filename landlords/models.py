from django.db import models

# Create your models here.
class Landlord(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15) # verbose_name = 'Mobile'
	email = models.EmailField(max_length=255)

	def __unicode__(self):
		return self.name

class Room(models.Model):
	address = models.CharField(max_length=20)
	rent = models.DecimalField(max_digits=3, decimal_places=0)
	postcode = models.CharField(max_length=50, blank=True)
	pet_allowed = models.BooleanField(default=False)
	landlord = models.ForeignKey(Landlord)

	def __unicode__(self):
		return self.address

	class Meta:
		ordering = ['rent']

class Message(models.Model):
	content = models.CharField(max_length=255)
	tenant = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	date_time = models.DateTimeField()
	landlord = models.ForeignKey(Landlord) 
