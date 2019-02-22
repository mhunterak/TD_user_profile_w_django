import re

from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from .models import Profile


class NotSamePassword(object):
    def validate(self, password, user=None):
        if user is not None and user.password is not None:
            if check_password(password, user.password):
                raise ValidationError(
                    _("The password must not be the same as the current password."),
                    code='not_same_as_current',
                )

    def get_help_text(self):
        return _(
            "Your password must not be the same as the current password."
        )


class ContainsUpperLowerNumberSpecial(object):
    def validate(self, password, user=None):
        if not re.match('(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)', password):
            raise ValidationError(
                _("The password must use at least one of each: uppercase letter, lowercase letter, number and special character."),
                code='upper_lower_number_special',
            )

    def get_help_text(self):
        return _(
            "Your The password must use at least one of each: uppercase letter, lowercase letter, number and special character."
        )


NameInPWerr = "Your Password cannot contain user name or parts of full name."


class NameNotInPassword(object):
    def validate(self, password, user=None):
        flag = 0
        if user.username in password:
            flag += 1
            print('username in password flag')
            print('{} in {}'.format(user.username, password))
        try:
            profile = Profile.objects.get(user)
            if profile.first_name != "":
                if re.match(profile.first_name, password):
                    print('firstname in password flag')
                    flag += 1
            if profile.last_name != "":
                if re.match(profile.last_name, password):
                    print('lastname in password flag')
                    flag += 1
        except (TypeError, Profile.DoesNotExist):
            '''
            If they don't have a profile yet, I think it's okay to skip
            this password validation test.
            '''
            pass
        if flag > 0:
            print("{} flags".format(flag))
            raise ValidationError(
                _(NameInPWerr),
                code='contains_name',
            )

    def get_help_text(self):
        return _(NameInPWerr)
