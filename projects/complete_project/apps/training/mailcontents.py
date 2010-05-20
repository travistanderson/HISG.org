# mail-contents.py
from training.models import EmailTemplate, Event


# here are the defaults for a success confirmation email after someone signs up
def sumail(event,user):
	SU_FROMEMAIL = str(event.contact.email)
	SU_TOEMAIL = [str(user.email),"cjennings@hisg.org","smix@hisg.org",str(event.contact.email)]
	SU_SUBJECT = "HISG signup confirmation email for "+str(event)+"."
	# SU_CONTENT = "Dear "+str(user.first_name)+",\n\nThank you for registering to attend "+str(event)+". It will begin on "+event.start_date.strftime("%b. %d, %Y")+" and end on "+event.end_date.strftime("%b. %d, %Y")+". As the event approaches, you will receive a follow-up email confirming last minute details."+str(event.contact)+" is the contact person for this training event, please contact him/her at "+str(event.contact.email)+" with any questions you may have. Thank you for signing up. We will see you there. \n\Sincerely,\nHISG Training Staff."
	# event.start_date.strftime("%b. %d"),event.end_date.strftime("%d, %Y")
	start_date = event.start_date
	end_date = event.end_date
	if start_date == end_date:
		thedate = '''on %s''' %(start_date.strftime("%b. %d, %Y"))
	else:
		if start_date.month == end_date.month:
			thedate = '''from %s-%s''' %(start_date.strftime("%b. %d"),event.end_date.strftime("%d, %Y"))
		else:
			thedate = '''from %s-%s''' %(start_date.strftime("%b. %d"),event.end_date.strftime("%b. %d, %Y"))
		
	SU_CONTENT = '''Dear %s,
	
	Thank you for registering to attend the training in %s %s. 
As the event approaches, you will receive a follow-up email confirming final details. %s (%s) or Charlene Jennnings (cjennings@hisg.org) are the contact people for this training event. Please contact them should you have any questions.

Thank you for signing up. We look forward to seeing you soon!

	
HISG Training Staff	''' %(str(user.first_name),str(event.location),thedate,str(event.contact),str(event.contact.email))

	return SU_SUBJECT, SU_CONTENT, SU_FROMEMAIL, SU_TOEMAIL
	


# here are the defaults for a success cancelation email after someone cancels a registration
def cancelmail(event,user):
	SU_FROMEMAIL = str(event.contact.email)
	SU_TOEMAIL = [str(user.email),"cjennings@hisg.org",str(event.contact.email)]
	SU_SUBJECT = "HISG Event Cancellation email for "+str(event)+"."
	# SU_CONTENT = "Dear " + str(user.first_name) + ", \n \n \n We have received your registration cancellation for the "+str(event)+" training event. We are sorry that you are unable to attend this training workshop, but we look forward to seeing you at future training events. Please check http://hisg.org/training-and-models/training for more information on upcoming events.  \n \n Sincerely, \n \n HISG Training Staff"
	SU_CONTENT = '''Dear %s, 

	We have received your registration cancellation for the %s training event. We are sorry that you are unable to attend this training workshop, but we look forward to seeing you at future training events. Please check http://hisg.org/training-and-models/training for more information on upcoming events.

Sincerely,
HISG Training Staff''' %(str(user.first_name),str(event))
	
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
	
	
