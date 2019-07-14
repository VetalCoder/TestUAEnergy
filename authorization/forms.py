from django.contrib.auth.forms import AuthenticationForm
from django.forms import ValidationError
from django.utils.translation import gettext as _


class UserEnergyForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(_("Access denied"))
        if user.username != 'uaenergy':
            raise ValidationError(_("You can't login with this account."))
