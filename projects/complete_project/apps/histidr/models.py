# histidr/models.py
from django.db import models
from datetime import datetime, timedelta

HISTIDR = (
    ('HIST', 'HIST',),
    ('IDR', 'IDR',),
)


class HistIdr(models.Model):

	histidr = models.CharField(max_length = 200, choices=HISTIDR, default=1)
	hist1 = models.BooleanField(default=False, verbose_name="Agriculture and Animal Husbandry",)
	hist2 = models.BooleanField(default=False, verbose_name="Arts and Entertainment",)
	hist3 = models.BooleanField(default=False, verbose_name="Economic Development",)
	hist4 = models.BooleanField(default=False, verbose_name="Information, Communications, Technology",)
	hist5 = models.BooleanField(default=False, verbose_name="Education",)
	hist6 = models.BooleanField(default=False, verbose_name="Family Development, Support",)
	hist7 = models.BooleanField(default=False, verbose_name="Government",)
	hist8 = models.BooleanField(default=False, verbose_name="Security, Justice, and the Rule of Law",)
	hist9 = models.BooleanField(default=False, verbose_name="Health, Hygiene",)
	hist10 = models.BooleanField(default=False, verbose_name="Medical",)
	hist11 = models.BooleanField(default=False, verbose_name="Infrastructure",)
	hist12 = models.BooleanField(default=False, verbose_name="Non-Profit Organizations",)
	idr1 = models.BooleanField(default=False, verbose_name="Water Services",)
	idr2 = models.BooleanField(default=False, verbose_name="Food Services",)
	idr3 = models.BooleanField(default=False, verbose_name="Shelter Services",)
	idr4 = models.BooleanField(default=False, verbose_name="Medical Services",)
	idr5 = models.BooleanField(default=False, verbose_name="Individual Assistance Services",)
	idr6 = models.BooleanField(default=False, verbose_name="Personal Hygiene Services",)
	idr7 = models.BooleanField(default=False, verbose_name="Counseling and Spiritual Support",)
	idr8 = models.BooleanField(default=False, verbose_name="Physical Reconstruction Services",)
	idr9 = models.BooleanField(default=False, verbose_name="Logistics Management and Services",)
	idr10 = models.BooleanField(default=False, verbose_name="IT, Telecommunications",)
	idr11 = models.BooleanField(default=False, verbose_name="Special Needs Services",)
	idr12 = models.BooleanField(default=False, verbose_name="Donations Management",)
	idr13 = models.BooleanField(default=False, verbose_name="Professional Responders",)
	idr14 = models.BooleanField(default=False, verbose_name="Transition and Recovery",)

	def __unicode__(self):
		unic = "" + self.histidr
		if self.hist1:
			unic = unic + ", Agriculture and Animal Husbandry"
		if self.hist2:
			unic = unic + ", Arts and Entertainment"
		if self.hist3:                  
			unic = unic + ", Economic Development"
		if self.hist4:                  
			unic = unic + ", Information, Communications, Technology"
		if self.hist5:                  
			unic = unic + ", Education"
		if self.hist6:                  
			unic = unic + ", Family Development, Support"
		if self.hist7:                  
			unic = unic + ", Government"
		if self.hist8:                  
			unic = unic + ", Security, Justice, and the Rule of Law"
		if self.hist9:                  
			unic = unic + ", Health, Hygiene"
		if self.hist10:                 
			unic = unic + ", Medical"
		if self.hist11:                 
			unic = unic + ", Infrastructure"
		if self.hist12:                 
			unic = unic + ", Non-Profit Organizations"
		if self.idr1:                   
			unic = unic + ", Water Services"
		if self.idr2:                   
			unic = unic + ", Food Services"
		if self.idr3:                   
			unic = unic + ", Shelter Services"
		if self.idr4:                   
			unic = unic + ", Medical Services"
		if self.idr5:                   
			unic = unic + ", Individual Assistance Services"
		if self.idr6:                   
			unic = unic + ", Personal Hygiene Services"
		if self.idr7:                   
			unic = unic + ", Counseling and Spiritual Support"
		if self.idr8:                   
			unic = unic + ", Physical Reconstruction Services"
		if self.idr9:                   
			unic = unic + ", Logistics Management and Services"
		if self.idr10:                   
			unic = unic + ", IT, Telecommunications"
		if self.idr11:                   
			unic = unic + ", Special Needs Services"
		if self.idr12:                   
			unic = unic + ", Donations Management"
		if self.idr13:                   
			unic = unic + ", Professional Responders"
		if self.idr14:                   
			unic = unic + ", Transition and Recovery"
		return unic




# return "%s with %s" % (self.histidr, self.histpic)

# HISTIDR = (
#     ('HIST', 'HIST',),
#     ('IDR', 'IDR',),
# )
# 
# class HistPic(models.Model):
# 
# 	name = models.CharField(max_length = 200)
# 	shortname = models.CharField(max_length = 10)
# 	subcat1 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat2 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat3 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat4 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat5 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat6 = models.CharField(max_length = 200, null=True, blank=True)
# 
# 	def __unicode__(self):
# 		return self.name
# 
# class IdrPic(models.Model):
# 
# 	name = models.CharField(max_length = 200)
# 	shortname = models.CharField(max_length = 10)
# 	subcat1 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat2 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat3 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat4 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat5 = models.CharField(max_length = 200, null=True, blank=True)
# 	subcat6 = models.CharField(max_length = 200, null=True, blank=True)
# 
# 	def __unicode__(self):
# 		return self.name
# 
# class HistIdr(models.Model):
# 
# 	histidr = models.CharField(max_length = 200, choices=HISTIDR, default=1)
# 	histpic = models.ManyToManyField(HistPic, null=True, blank=True)
# 	idrpic = models.ManyToManyField(IdrPic, null=True, blank=True)
# 	
# 	# for i in range(1,6):
# 	# 	display += 
# 	display = histpic
# 
# 	def __unicode__(self):
# 		return self.histidr