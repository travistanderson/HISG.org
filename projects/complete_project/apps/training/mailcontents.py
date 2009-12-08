# mail-contents.py

# here are the defaults for a success confirmation email after someone signs up
def sumail(event,user):
	SU_SUBJECT = "HISG Training confirmation email."
	SU_CONTENT = "Thank you for registering to attend"+str(event.name)+"."
	SU_FROMEMAIL = 'cjennings@hisg.org'
	SU_TOEMAIL = [str(user.email)]
	return SU_SUBJECT, SU_CONTENT, SU_FROMEMAIL, SU_TOEMAIL
	
