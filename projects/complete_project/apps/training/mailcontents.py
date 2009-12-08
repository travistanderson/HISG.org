# mail-contents.py

# here are the defaults for a success confirmation email after someone signs up
def sumail(event,user):
	SU_FROMEMAIL = str(event.contact.email)
	SU_TOEMAIL = [str(user.email)]
	SU_SUBJECT = "HISG signup confirmation email for "+str(event)+"."
	SU_CONTENT = "Thank you for registering to attend "+str(event)+". It will begin on "+event.start_date.strftime("%b. %d, %Y")+" and end on "+event.start_date.strftime("%b. %d, %Y")+". As the event approaches, you will receive a follow-up email confirming last minute details."+str(event.contact)+" is the contact person for this training event, please contact him/her at "+str(event.contact.email)+" with any questions you may have. Thank you for signing up. We will see you there. HISG Training Staff."
	return SU_SUBJECT, SU_CONTENT, SU_FROMEMAIL, SU_TOEMAIL
	
