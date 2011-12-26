
NAVLINKS=([u'/', 'Welcome'],
		  [u'/about_us.html', 'About us'],
		  [u'/party.html','Wedding party'],
		  [u'/travel.html','Travel and Lodging'],
		  [u'/gifts.html', 'Gifts'],
		  [u'/songs/', "What's your favorite wedding song?"]
		  )
		  
		  
class NavLink(object):
	def __init__(self, href, title, current = False):
		self.href=href
		self.title=title
		self.current=current
		
	def as_html(self):
		if self.current:
			return u"<li class='current'>%s</li>" % (self.title)
		else:
			return u"<li > <a href='%s'>%s</a></li>" % (self.href, self.title)



def nav_context(request):
	links=[]
	#import pdb;pdb.set_trace()
	for href, title in NAVLINKS:
		links.append(NavLink(href, title, href == request.path_info))
		
	return {'navlinks': links}