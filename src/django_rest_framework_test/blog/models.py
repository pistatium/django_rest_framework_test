from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__


class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
            (STATUS_DRAFT, "下書き"),
            (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name='entries')

    def __repr__(self):
        return "{}: {}".format(self.pk, self.title)

    __str__ = __repr__
