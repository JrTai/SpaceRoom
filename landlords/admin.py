from django.contrib import admin
from landlords.models import Landlord, Room, Message

# Register your models here.
class LandlordAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'email')
	search_fields = ('name',)

class RoomAdmin(admin.ModelAdmin):
	list_display = ('address', 'rent', 'postcode', 'pet_allowed', 'landlord')
	list_filter = ('pet_allowed',)
	#fields = ('rent', 'pet_allowed', 'landlord') # allowed to be modify
	ordering = ('-rent',)

class MessageAdmin(admin.ModelAdmin):
	list_display = ('tenant', 'content', 'email', 'date_time', 'landlord')

admin.site.register(Landlord, LandlordAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)

