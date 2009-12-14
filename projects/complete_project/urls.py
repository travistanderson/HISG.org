from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin

import os.path

#from zwitschern.feeds import TweetFeedAll, TweetFeedUser, TweetFeedUserWithFriends
#tweets_feed_dict = {"feed_dict": {
#    'all': TweetFeedAll,
#    'only': TweetFeedUser,
#    'with_friends': TweetFeedUserWithFriends,
#}}

# from zwitschern.feeds import TweetFeedAll, TweetFeedUser, TweetFeedUserWithFriends
# tweets_feed_dict = {"feed_dict": {
#     'all': TweetFeedAll,
#     'only': TweetFeedUser,
#     'with_friends': TweetFeedUserWithFriends,
# }}

# from blog.feeds import BlogFeedAll, BlogFeedUser
# blogs_feed_dict = {"feed_dict": {
#     'all': BlogFeedAll,
#     'only': BlogFeedUser,
# }}

from bookmarks.feeds import BookmarkFeed
bookmarks_feed_dict = {"feed_dict": { '': BookmarkFeed }}

from newsphotos.models import News
news_dict = {"queryset": News.objects.all().order_by('-date'),}

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('homepage.urls')),
    
    (r'^training-and-models/', include('training.urls')),
    (r'^initiatives/', include('featured.urls')),
    (r'^projects-and-news/', include('projectsmodels.urls')),
    (r'^about-hisg/', include('about.urls')),
    (r'^donation-portal/', include('donationportal.urls')),
    (r'^account/', include('account.urls')),
    (r'^comments/', include('threadedcomments.urls')),
    (r'^robots.txt$', include('robots.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^photologue/', include('photologue.urls')),
	(r'^user/', include('tiq_login.urls')),
    # (r'^profiles/', include('profiles.urls')),
	(r'^info/', include('faqs.urls')),
	(r'^projects-and-models/', include('training.urls')),# this is a redirect for the email about training

	(r'^admin/training/event/tableview/', include('training.admin_urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^photos/', include('photos.urls')),
    (r'^search/', include('lookfor.urls')),
)


from photos.models import Image

friends_photos_kwargs = {
    "template_name": "photos/friends_photos.html",
    "friends_objects_function": lambda users: Image.objects.filter(member__in=users),
}

from blog.models import Post

friends_blogs_kwargs = {
    "template_name": "blog/friends_posts.html",
    "friends_objects_function": lambda users: Post.objects.filter(author__in=users),
}

# from zwitschern.models import Tweet
# 
# friends_tweets_kwargs = {
#     "template_name": "zwitschern/friends_tweets.html",
#     "friends_objects_function": lambda users: Tweet.objects.filter(sender__in=users),
# }

from bookmarks.models import Bookmark

friends_bookmarks_kwargs = {
    "template_name": "bookmarks/friends_bookmarks.html",
    "friends_objects_function": lambda users: Bookmark.objects.filter(saved_instances__user__in=users),
    "extra_context": {
        "user_bookmarks": lambda request: Bookmark.objects.filter(saved_instances__user=request.user),
    },
}
# 
# urlpatterns += patterns('',
#     url('^photos/friends_photos/$', 'friends_app.views.friends_objects', kwargs=friends_photos_kwargs, name="friends_photos"),
#     url('^blog/friends_blogs/$', 'friends_app.views.friends_objects', kwargs=friends_blogs_kwargs, name="friends_blogs"),
#     url('^tweets/friends_tweets/$', 'friends_app.views.friends_objects', kwargs=friends_tweets_kwargs, name="friends_tweets"),
#     url('^bookmarks/friends_bookmarks/$', 'friends_app.views.friends_objects', kwargs=friends_bookmarks_kwargs, name="friends_bookmarks"),
# )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "site_media")}),
    )
