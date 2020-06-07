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

    def test_get_failure_no_post(self):
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
            # We now have 1 like on the post.
            "likes": 1,
        }

        self.assertEqual(get_post_response.json(), expected)

    def test_post_failure_no_post_id(self):
        c = Client()

        # No `post_id` provided.
        response = c.post("/like", {}, content_type="application/json")

        self.assertEqual(response.status_code, 500)


class LikeTransactionTestCase(TransactionTestCase):
    def test_post_failure_invalid_post_id(self):
        c = Client()

        # This post does not exists.
        response = c.post("/like", {"post_id": 2}, content_type="application/json")

        self.assertEqual(response.status_code, 500)
