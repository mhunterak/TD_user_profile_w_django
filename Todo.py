'''
MASTER TODO LIST for User Profile project
'''

# Create a Django model for the user profile.
# Add routes to display a profile,
# edit a profile,
# and change the password.

# Create a “profile” view to display a user profile
# with the following fields:
# First Name,
# Last Name,
# Email,
# Date of Birth,
# Bio and
# Avatar
# Include a link to edit the profile.

# Create an “edit” view with the route “/profile/edit”
# that allows the user to edit the user profile with the following fields:
# First Name,
# Last Name,
# Email,
# Date of Birth,
# Confirm Email,
# Bio and
# Avatar.

# Validate user input "Date of Birth" field:
# check for a proper date format (YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY)
# Validate user input "Email" field: check that
# the email addresses match and are in a valid format.
# Validate user input "Bio" field: check that the bio is
# 10 characters or longer and properly escapes HTML formatting.

# Use the supplied HTML/CSS to build and style the
# profile page
# bio page.

# Add the ability to upload and save a user’s avatar image.

''' TODO: Create “change-password” view with the route
    # “/profile/change_password” that allows the user to update their password
    # using User.set_password() and then User.save(). Form fields will be:
    # current password, new password, confirm password
    # TODO: Validate user input "Password" fields: check that the old
    # password is correct using User.check_password() and the
    # new password matches the confirm password field and
    # follows the following password policy:
    # TODO: must not be the same as the current password
    # minimum password length of 14 characters
    # TODO: must use of both uppercase and lowercase letters
    # TODO: must include one or more numerical digits
    # TODO: must include one or more of special characters, such as @, # , $
    # TODO: cannot contain the user name or parts of the user’s full name,
    # such as their first name
'''
# TODO: Use CSS to style headings, font, and form.
# TODO: Make sure your coding style complies with PEP 8

''' TODO: EXTRA CREDIT
# TODO: Add additional form fields to build a more complex form
# with additional options, such as city/state/country of residence,
# favorite animal or hobby,
# TODO: JavaScript is utilized for a date dropdown for
# the Date of Birth validation feature.
# TODO: JavaScript is utilized for text formatting for
# the Bio validation feature.
# TODO: Add an online image editor to the avatar.
# Include the basic functionality: rotate, crop and flip. PNG mockup supplied.
# TODO: A password strength “meter” is displayed when validating passwords.
'''
