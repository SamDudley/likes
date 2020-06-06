from django.test import TestCase, TransactionTestCase, Client

from likes.models import Post


class PostTestCase(TestCase):
    def test_get_success(self):
        c = Client()

        response = c.get("/post")

        expected = {
            "id": 1,
            "content": "This is the first post and it's wonderful.",
            "likes": 0,
        }

        self.assertEqual(response.json(), expected)

    def test_get_failure(self):
        Post.objects.all().delete()

        c = Client()

        response = c.get("/post")

        self.assertEqual(response.status_code, 500)


class LikeTestCase(TestCase):
    def test_post_success(self):
        c = Client()

        post_like_response = c.post(
            "/like", {"post_id": 1}, content_type="application/json"
        )

        self.assertEqual(post_like_response.status_code, 200)

        get_post_response = c.get("/post")

        expected = {
            "id": 1,
            "content": "This is the first post and it's wonderful.",
            "likes": 1,
        }

        self.assertEqual(get_post_response.json(), expected)


class LikeTransactionTestCase(TransactionTestCase):
    def test_post_failure(self):
        c = Client()

        response = c.post("/like", {"post_id": 2}, content_type="application/json")

        self.assertEqual(response.status_code, 500)
