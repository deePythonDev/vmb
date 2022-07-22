from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import CharField, BooleanField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from allauth.account.models import EmailAddress
from django.db import models

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), max_length=255, blank=True)
    phone = CharField(
        _("Phone"),
        max_length=17,
        validators=[
            RegexValidator(
                regex=r"^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
            )
        ],
        blank=True,
    )
    is_matrimony_candidate = BooleanField(
        _("Is matrimony candidate?"), default=False, blank=True
    )
    is_matrimony_registration_complete = BooleanField(
        _("Is matrimony registration complete?"), default=False, blank=True
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def send_confirmation_email(self):
        email, _ = EmailAddress.objects.get_or_create(user=self, email=self.email)
        email.send_confirmation(signup=True)
        
class UserNotificationPreference(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    email_announcements = BooleanField(_("Announcements"), default=True, null=False)
    email_matrimony = BooleanField(_("Matches Suggested"), default=True, null=False)
    
    def __str__(self):
        return f"{self.user}"
