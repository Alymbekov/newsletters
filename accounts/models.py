from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


def upload_to(instance, filename):
    return 'profile_images/{0}/{1}'.format(instance.user.pk, filename)


class Profile(models.Model):
    EXPERIENCE_CHOICES = (
        ('Меньше года', 'Меньше года'),
        ('1 до 3 лет', '1 до 3 лет'),
        ('Больше трёх лет', 'Больше трёх лет')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    career = models.CharField(max_length=255, blank=True)
    my_send_messages = models.TextField(blank=True)
    default_profile_image = 'profile.jpg'
    avatar = models.ImageField(
        default=default_profile_image,
        upload_to=upload_to,
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



