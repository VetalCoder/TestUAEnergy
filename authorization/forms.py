from django.contrib.auth.forms import AuthenticationForm
from django.forms import ValidationError


class UserEnergyForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError("Access denied")
        if user.username != 'test' and user.username != 'uaenergy':  # TODO: delete test case
            raise ValidationError("You can't login with this account.")
