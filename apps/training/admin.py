# training/admin.py
from django.contrib import admin
from training.models import Answer, BadgePhoto, Choice, Email, EventSubject, EmailTemplate, Event, Question, QuestionOrder, QuestionSet, SignupDate
from training.forms import EventAdminModelForm

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('user','event','question','answer')
	list_filter = ('event', 'user','question',)


class BadgePhotoAdmin(admin.ModelAdmin):
	list_display = ('name','user','admin_thumbnail',)
	ordering = ('user',)
	search_fields = ('name','user',)

class EventAdmin(admin.ModelAdmin):
	form = EventAdminModelForm
	search_fields = ('location','start_date',)
	list_filter = ('start_date','contact',)
	list_display = ('id','location','start_date','contact','tableview','active')
	list_display_links = ('location',)
	ordering = ('-start_date',)
	filter_horizontal = ('attendee','registrant','eventsubject',)
	fieldsets = (
		(None, {'fields': (('location', 'active','latitude','longitude',),),'classes':('wide',)}),
		(None, {'fields': ('description',),'classes':('wide',)}),
		# ('Date Information', {'fields': }),
		(None, {'fields': (('contact', 'subject',),('start_date', 'end_date',))}),
		('Extras', {'fields': ('registrant', 'attendee','questionset','limit','eventsubject','start_date_register','end_date_register',),'classes': ('collapse',),}),
	)
	change_form_template = 'admin/training/event/change_form.html'
	save_on_top = True



class QuestionAdmin(admin.ModelAdmin):
	list_display = ('id','qtype','question',)
	list_display_links = ('question',)
	ordering = ('id',)
	filter_horizontal = ('multi','radio',)	
	fieldsets = (
		(None, {'fields': ('question', 'help_text','required','qtype',),}),
		('Multi', {'fields': ('multi',),}),
		('Radio', {'fields': ('radio',),}),
		('Text', {'fields': ('rows',),}),
	)

class QuestionSetAdmin(admin.ModelAdmin):
	list_display = ('name','id','howmany',)
	filter_horizontal = ('questions',)
	
	
class QuestionOrderAdmin(admin.ModelAdmin):
	list_display = ('questionset','order','question',)
	ordering = ('questionset','order',)
	

	
	
class SignupDateAdmin(admin.ModelAdmin):
	list_display = ('event','user','date',)	
	ordering = ('event',)
	

admin.site.register(Answer, AnswerAdmin)
admin.site.register(BadgePhoto, BadgePhotoAdmin)
admin.site.register(Choice)
admin.site.register(Email)
admin.site.register(EventSubject)
admin.site.register(EmailTemplate)
admin.site.register(Event, EventAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionOrder, QuestionOrderAdmin)
admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(SignupDate, SignupDateAdmin)

