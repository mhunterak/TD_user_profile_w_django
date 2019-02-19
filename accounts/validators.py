import re
from string import punctuation

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.hashers import check_password


class NotSamePassword(object):
    def validate(self, password, user=None):
        if check_password(password, user.password):
            raise ValidationError(
                _("The password must not be the same as the current password."),
                code='not_same_as_current',
            )

    def get_help_text(self):
        return _(
            "Your password must not be the same as the current password."
        )


class UpperAndLowerCase(object):
    def validate(self, password, user=None):
        has_lower = False
        has_upper = False
        for letter in list(password):
            while not has_lower:
                if re.match('[a-z]', password):
                    has_lower = True
            while not has_upper:
                if re.match('[A-Z]', password):
                    has_upper = True
        if not (has_upper and has_lower):
            raise ValidationError(
                _("The password must use of both uppercase and lowercase letters."),
                code='upper_and_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must use of both uppercase and lowercase letters."
        )


class ContainsNumbers(object):
    def validate(self, password, user=None):
        numberOfDigits = 0
        for letter in list(password):
            if letter.isdigit():
                numberOfDigits += 1
        if numberOfDigits == 0:
            raise ValidationError(
                _("The password must include one or more numerical digits."),
                code='contains_number',
            )

    def get_help_text(self):
        return _("Your password must include one or more numerical digits.")


class ContainsSpecialChar(object):
    def validate(self, password, user=None):
        numberOfSpecialChar = 0
        for letter in list(password):
            if letter in set(punctuation):
                numberOfSpecialChar += 1
        if numberOfSpecialChar == 0:
            raise ValidationError(
                _("The password must include one or more special characters, such as @, # , $."),
                code='contains_special',
            )

    def get_help_text(self):
        return _("Your password must include one or more special characters.")


class NameNotInPassword(object):
    def validate(self, password, user=None):
        flag = 0
        if user.username in password:
            flag += 1
        if user.profile.first_name in password:
            flag += 1
        if user.profile.last_name in password:
            flag += 1
        if flag > 0:
            raise ValidationError(
                _("Your Password cannot contain user name or parts of the full name."),
                code='contains_namw',
            )

    def get_help_text(self):
        return _("Your password must include one or more special characters.")
