# donationportal/admin.py
from django.contrib import admin
from donationportal.models import Donation
from videos.models import Video
from photologue.models import Photo

class PhotoInline(admin.TabularInline):
	model = Photo
	
class VideoInline(admin.TabularInline):
	model = Video

class DonationAdmin(admin.ModelAdmin):

	list_display = ('name', 'description', 'paypal',)

admin.site.register(Donation, DonationAdmin)
