import datetime
from haystack import indexes
from haystack import site
from about.models import Office, Staff

class OfficeIndex(indexes.SearchIndex):
    name = indexes.CharField(document=True)

    def get_query_set(self):
        return Office.objects.all()


class StaffIndex(indexes.SearchIndex):
    email = indexes.CharField(document=True, use_template=True)

    def get_query_set(self):
        return Staff.objects.all()

site.register(Office, OfficeIndex)
site.register(Staff, StaffIndex)
