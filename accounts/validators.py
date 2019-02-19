import re
from string import punctuation

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.hashers import check_password

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


class NameNotInPassword(object):
    def validate(self, password, user=None):
        flag = 0
        if user.username in password:
            flag += 1
        profile = Profile.create_or_recall(user)
        if profile.first_name != "":
            if re.match(profile.first_name, password):
                flag += 1
        if profile.last_name != "":
            if re.match(profile.last_name, password):
                flag += 1
        if flag > 0:
            print("{} flags".format(flag))
            raise ValidationError(
                _("Your Password cannot contain user name or parts of the full name."),
                code='contains_namw',
            )

    def get_help_text(self):
        return _("Your Password cannot contain user name or parts of the full name.")
