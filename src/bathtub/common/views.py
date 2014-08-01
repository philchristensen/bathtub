from django import shortcuts

from . import Show

def home(request):
	return shortcuts.render_to_response('scripts/list.html', dict(
		title			= "shows",
		shows			= models.Show.objects.all()
	), context_instance=template.RequestContext(request))
