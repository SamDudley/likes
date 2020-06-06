import json

from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from likes.models import Post, Like


class BaseView(View):
    def dispatch(self, req: HttpRequest, *args, **kwargs) -> HttpResponse:
        req.json = json.loads(req.body) if req.body else {}

        response = super().dispatch(req, *args, **kwargs)

        # Basic CORS to get us going.
        response["Access-Control-Allow-Origin"] = req.headers.get("Origin", "")
        response["Access-Control-Allow-Headers"] = "Content-Type"

        return response


class PostView(BaseView):
    def get(self, req: HttpRequest) -> JsonResponse:
        post = Post.objects.first()

        if not post:
            return HttpResponse(status=500)

        return JsonResponse(
            {"id": post.id, "content": post.content, "likes": post.likes.count()}
        )


@method_decorator(csrf_exempt, name="dispatch")
class LikeView(BaseView):
    def post(self, req: HttpRequest) -> HttpResponse:
        post_id = req.json["post_id"]

        try:
            Like.objects.create(post_id=post_id)
        except IntegrityError:
            return HttpResponse(status=500)

        return HttpResponse(status=200)
