from django.test import TestCase, Client


class PostTestCase(TestCase):
    def test_post(self):
        c = Client()

        response = c.get("/post")

        expected = {
            "id": 1,
            "content": "This is the first post and it's wonderful.",
            "likes": 0,
        }

        self.assertEqual(response.json(), expected)

    def test_like_post(self):
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
