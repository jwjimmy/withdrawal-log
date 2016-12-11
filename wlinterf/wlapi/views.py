from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from wlapi.models import Visit
from django.http import JsonResponse
from django.views.generic.edit import CreateView
#from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context

class VisitView(ListView):

    model = Visit

class VisitCreate(CreateView):

    model = Visit
    fields = ['visited_at', 'reason']

class HomeView(TemplateView):

    template_name = 'wlapi/home.html'