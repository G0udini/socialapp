from .models import Profile


def connect_profile(backend, user, response, *args, **kwargs):
    if kwargs["is_new"]:
        Profile.objects.create(user=user)
