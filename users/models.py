from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from activation.signals import set_inactive_user

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, is_social_user=False):
        if not email:
            raise ValueError('Users must have an e-mail address.')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        if not is_social_user:
            set_inactive_user.send(sender=settings.AUTH_USER_MODEL, user=user)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name):
        user = self.create_user(email, first_name, last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class MyUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, null=False, max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return str(self.user)


class ContactApp(models.Model):
    title = models.CharField(max_length=255, default="Traiesc sa transform imposibilul in posibil")
    envelope_message = models.CharField(max_length=255, default="Te invit sa stam de vorba")
    contact_info = models.CharField(max_length=255, default="Informatii de contact")
    location = models.CharField(max_length=255, default="Cugir, Romania")
    phone = models.CharField(max_length=255, default="0769370793")
    email = models.CharField(max_length=255, default="boanca_ionut_silviu@yahoo.com")
    link_facebook = models.CharField(max_length=255, default=None, blank=True)
    link_youtube = models.CharField(max_length=255, default=None, blank=True)
    link_linkedin = models.CharField(max_length=255, default=None, blank=True)
    link_instagram = models.CharField(max_length=255, default=None, blank=True)

    def __str__(self):
        return self.title


class EnContactApp(models.Model):
    title = models.CharField(max_length=255, default="Title for contact from")
    envelope_message = models.CharField(max_length=255, default="Lets talk")
    contact_info = models.CharField(max_length=255, default="Contact Info")
    location = models.CharField(max_length=255, default="Cugir, Romania")
    phone = models.CharField(max_length=255, default="0040769370793")
    email = models.CharField(max_length=255, default="boanca_ionut_silviu@yahoo.com")
    link_facebook = models.CharField(max_length=255, default=None, blank=True)
    link_youtube = models.CharField(max_length=255, default=None, blank=True)
    link_linkedin = models.CharField(max_length=255, default=None, blank=True)
    link_instagram = models.CharField(max_length=255, default=None, blank=True)

    def __str__(self):
        return self.title


class RoNewsletter(models.Model):
    email = models.EmailField(unique=False, null=False, max_length=255)

    def __str__(self):
        return self.email
