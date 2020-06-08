import json

from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from likes.models import Post, Like


class BaseView(View):
    def dispatch(self, req: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = super().dispatch(req, *args, **kwargs)

        # Basic CORS to get us going.
        # TODO: Add comprehensive CORS.
        response["Access-Control-Allow-Origin"] = req.headers.get("Origin", "")
        response["Access-Control-Allow-Headers"] = "Content-Type"

        return response


class PostView(BaseView):
    def get(self, req: HttpRequest) -> JsonResponse:
        """Return the first post and the like count.

        API Response:
            {
                "id": int,
                "content": str,
                "likes": int,
            }

            Returns a 500 if no post is found.

        Args:
            req (HttpRequest): Django HTTP request

        Returns:
            JsonResponse: Post and like count JSON
        """
        # We have a data migration that provides the first and only post.
        # backend/likes/migrations/0002_auto_20200606_1240.py
        post = Post.objects.first()

        if not post:
            return HttpResponse(status=500)

        return JsonResponse(
            {"id": post.id, "content": post.content, "likes": post.likes.count()}
        )


# TODO: Decide whether we are going to use CSRF tokens with a REST API.
@method_decorator(csrf_exempt, name="dispatch")
class LikeView(BaseView):
    def post(self, req: HttpRequest) -> HttpResponse:
        """Add a like for a post.

        API Request:
            {
                "post_id": int,
            }

        API Response:
            Status code 200 if success and 500 if error.

        Args:
            req (HttpRequest): Django HTTP request

        Returns:
            HttpResponse: Status code represents success
        """
        # TODO: Refactor into BaseView for all future post methods.
        req.json = json.loads(req.body) if req.body else {}

        post_id = req.json.get("post_id")

        if post_id is None:
            return HttpResponse(status=500)

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return HttpResponse(status=500)

        post.likes.create(post_id=post_id)

        return JsonResponse({"post_id": post_id, "likes": post.likes.count()})
