from django.db import models


class Post(models.Model):
    content = models.TextField()


class Like(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="likes")
