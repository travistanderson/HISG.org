from django.conf import settings
from django.contrib.auth.models import User, check_password, Group, Permission
from django.contrib.auth import login, authenticate
from clogin.models import CloginProfile
from xmlrpclib import ServerProxy

class CloginBackend:
	"""
	"""
	supports_objects_permissions = True

	def authenticate(self, sid):
		# jsonrequest = ServiceProxy(str(settings.JSONRPCIP))
		xmlrpcrequest = ServerProxy(str(settings.XMLRPCIP))
		# result = jsonrequest.login.getusernamej(un)
		# us = result['result']
		us = xmlrpcrequest.login.getusername(str(sid))
		
		try:
			user = User.objects.get(username=us['screen_name'])
			if us['is_superadmin']:
				user.is_staff = True
				user.is_superuser = True
			else:
				user.is_staff = False
				user.is_superuser = False
			user.first_name = us['full_name']
			user.last_name = us['uid']
			# user.session_id = sid
			user.email = us['email']
			user.save()
		except User.DoesNotExist:
			user = User(username=us['screen_name'], password='')
			user.set_unusable_password()
			user.email = us['email']
			if us['is_superadmin']:
				user.is_staff = True
				user.is_superuser = True
			else:
				user.is_staff = False
				user.is_superuser = False
			user.first_name = us['full_name']
			user.last_name = us['uid']
			# user.session_id = sid
			user.save()
		try:	
			profile = CloginProfile.objects.get(user=user)
		except CloginProfile.DoesNotExist:
			profile = CloginProfile.objects.create(user=user)
		profile = user.get_profile()
		profile.session_id = sid
		profile.signature = us['signature']
		profile.bio = us['bio']
		profile.save()
			
		return user


	def get_user(self, user_id):
		try:
			return User.objects.get(id=user_id)
		except User.DoesNotExist:
			return None



 
	# def get_group_permissions(self, user_obj):
	#	 """
	#	 Returns a set of permission strings that this user has through his/her
	#	 groups.
	#	 """
	#	 if not hasattr(user_obj, '_group_perm_cache'):
	#		 user_obj._group_perm_cache = set()
	#		 thegroup = user_obj.groups.select_related()
	#		 for gr in thegroup:
	#			 gp = gr.permissions.select_related()
	#			 # for perm in gp:
	#			 user_obj._group_perm_cache.update(gp)
	#	 return user_obj._group_perm_cache
	#  
	# def get_all_permissions(self, user_obj):
	#	 if not hasattr(user_obj, '_perm_cache'):
	#		 user_obj._perm_cache = set([u"%s.%s" % (p.content_type.app_label, p.codename) for p in user_obj.user_permissions.select_related()])
	#		 user_obj._perm_cache.update(self.get_group_permissions(user_obj))
	#	 return user_obj._perm_cache
	# 
	# def has_perm(self, user_obj, perm):
	#	 return perm in self.get_all_permissions(user_obj)
	# 
	# def has_module_perms(self, user_obj, app_label):
	#	 """
	#	 Returns True if user_obj has any permissions in the given app_label.
	#	 """
	#	 for perm in self.get_all_permissions(user_obj):
	#		 if perm[:perm.index('.')] == app_label:
	#			 return True
	#	 return False


