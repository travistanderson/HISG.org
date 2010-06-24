# featured/admin.py
from django.contrib import admin
from featured.models import HomerPager, HomerRev, Opportunity, RandyPage
from featured.forms import HomerPagerAdminModelForm, OpportunityAdminModelForm



class HomerPagerAdmin(admin.ModelAdmin):
	form = HomerPagerAdminModelForm
	list_display = ('last_edited',)

	
class OpportunityAdmin(admin.ModelAdmin):
	form = OpportunityAdminModelForm
	list_display = ('sorter','name','active','created',)
	list_display_links = ('name',)
	list_editable = ('sorter',)
	ordering = ('sorter',)
	# fieldsets = (
	# 	(None, {'fields': (('firstname','lastname','director',),('title','email','sorter',),('office','video',),'bio',)}),
	# 	(None, {'fields': ('photo',)}),
	# )


admin.site.register(HomerPager, HomerPagerAdmin)
admin.site.register(HomerRev)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(RandyPage)


