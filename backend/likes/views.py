import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View

from likes.models import Post, Like


class BaseView(View):
    def dispatch(self, req: HttpRequest, *args, **kwargs) -> HttpResponse:
        req.json = json.loads(req.body) if req.body else {}

        response = super().dispatch(req, *args, **kwargs)

        # Basic CORS to get us going.
        response["Access-Control-Allow-Origin"] = "*"

        return response


class PostView(BaseView):
    def get(self, req: HttpRequest) -> JsonResponse:
        post = Post.objects.first()

        return JsonResponse(
            {"id": post.id, "content": post.content, "likes": post.likes.count()}
        )


class LikeView(BaseView):
    def post(self, req: HttpRequest) -> HttpResponse:
        post_id = req.json["post_id"]

        Like.objects.create(post_id=post_id)

        return HttpResponse(status=200)
