# mail-contents.py
from training.models import EmailTemplate, Event


# here are the defaults for a success confirmation email after someone signs up
def sumail(event,user):
	SU_FROMEMAIL = str(event.contact.email)
	SU_TOEMAIL = [str(user.email),"cjennings@hisg.org",str(event.contact.email)]
	SU_SUBJECT = "HISG signup confirmation email for "+str(event)+"."
	SU_CONTENT = "Thank you for registering to attend "+str(event)+". It will begin on "+event.start_date.strftime("%b. %d, %Y")+" and end on "+event.end_date.strftime("%b. %d, %Y")+". As the event approaches, you will receive a follow-up email confirming last minute details."+str(event.contact)+" is the contact person for this training event, please contact him/her at "+str(event.contact.email)+" with any questions you may have. Thank you for signing up. We will see you there. HISG Training Staff."
	return SU_SUBJECT, SU_CONTENT, SU_FROMEMAIL, SU_TOEMAIL
	


# here are the defaults for a success cancelation email after someone cancels a registration
def cancelmail(event,user):
	SU_FROMEMAIL = str(event.contact.email)
	SU_TOEMAIL = [str(user.email),"cjennings@hisg.org",str(event.contact.email)]
	SU_SUBJECT = "HISG Event Cancelation email for "+str(event)+"."
	SU_CONTENT = "You have cancelled you registration for the "+str(event)+" training event. HISG Training Staff."
	return SU_SUBJECT, SU_CONTENT, SU_FROMEMAIL, SU_TOEMAIL
	
	
# here are the defaults for a sending a template from the admin
def templatemail(event,email_id):
	et = EmailTemplate.objects.get(id=email_id)
	eventname = str(event)
	eventsubject = event.subject
	eventdescription = event.description
	contactname = str(event.contact.firstname) + " " + str(event.contact.lastname)
	contactemail = event.contact.email
	
	SU_FROMEMAIL = str(event.contact.email)
	SU_SUBJECT = str(et.subject).replace('eventname',eventname).replace('eventsubject',eventsubject).replace('eventdescription',eventdescription).replace('contactname',contactname).replace('contactemail',contactemail)
	SU_CONTENT = str(et.content).replace('eventname',eventname).replace('eventsubject',eventsubject).replace('eventdescription',eventdescription).replace('contactname',contactname).replace('contactemail',contactemail)
	return SU_SUBJECT, SU_CONTENT, SU_FROMEMAIL
	
	
