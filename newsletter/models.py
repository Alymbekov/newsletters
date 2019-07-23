from django.db import models


class NewsLetterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    EMAIL_STATUS_CHOICES =(
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )

    subject = models.CharField(max_length=255)
    body = models.TextField()
    email = models.ManyToManyField(NewsLetterUser)
    status = models.CharField(max_length=15, choices=EMAIL_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject