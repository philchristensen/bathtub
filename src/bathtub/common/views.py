from django import shortcuts, template

from . import models

def home(request):
	return shortcuts.render_to_response('base.html', dict(
		title			= "shows",
		shows			= models.Show.objects.all()
	), context_instance=template.RequestContext(request))
