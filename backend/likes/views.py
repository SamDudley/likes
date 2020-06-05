from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View


class BaseView(View):
    def dispatch(self, req: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = super().dispatch(req, *args, **kwargs)

        # Basic CORS to get us going.
        response['Access-Control-Allow-Origin'] = '*'

        return response


class TestView(BaseView):
    def get(self, req: HttpRequest) -> JsonResponse:
        return JsonResponse({'message': 'Hello World!'})
