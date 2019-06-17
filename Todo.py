"""
MASTER TODO LIST for socail team builder project
"""
# As a user of the site, I should be able to sign up for an account.
# As a user of the site, I should be able to log into my account.
# As a user of the site, I should be able to edit my profile.
# As a user of the site, I should be able to upload an avatar image for my profile.
# As a user of the site, I should be able to pick my skills for my profile.
# As a user of the site, I should be able to create a project that I need help on.
# As a user of the site, I should be able to specify the positions my project needs help in with a name, a description, and related skill.
# As a user of the site, I should be able to see all of the applicants for my project's positions.
# As a user of the site, I should be able to approve an applicant for a position in my project.
# As a user of the site, I should be able to reject an applicant for a position in my project.
# As a user of the site, I should get a notification if I've been rejected or approved for a position.
# As a user of the site, I should be able to search for projects based on words in their titles or descriptions.
# As a user of the site, I should be able to filter projects by the positions they need filled.
# As a user of the site, I should be able to apply for a position in a project.
# As a user of the site, I should be able to log out.

# Extra Credit:

# TODO As a user of the site, I should get an email verification after sign up.
# As a user of the site, a position should be marked as filled once I accept someone for it.
# As a user of the site, I should filled positions should be hidden or marked as filled so I don't apply for them.
# As a user of the site, I should be able to use Markdown in the "about me" part of my profile.
# As a user of the site, I should be able to list any skill on my profile, not just pre-selected ones.
#  As a user of the site, my profile should list projects I've been involved with.
# TODO As a user of the site, I should be able to use Markdown in my project description.
# TODO As a user of the site, I should be able to use Markdown in the position descriptions.
# TODO As a user of the site, I should be able to provide a listed length of involvement for a position (e.g. Designer: 10 hours/week).
# TODO As a user of the site, I should be able to filter applicants by their status (approved, denied, undecided).
# As a user of the site, I should be able to approve or deny applicants directly from the list of applicants.
# TODO As a user of the site, I should be given a list of projects that need my skill set.


"""
MASTER TODO LIST for User Profile project
"""

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

# Create “change-password” view with the route
# “/profile/change_password” that allows the user to update their password
# using User.set_password() and then User.save(). Form fields will be:
# current password, new password, confirm password
# Validate user input "Password" fields: check that the old
# password is correct using User.check_password() and the
# new password matches the confirm password field and
# follows the following password policy:
# must not be the same as the current password
# minimum password length of 14 characters
# must use of both uppercase and lowercase letters
# must include one or more numerical digits
# must include one or more of special characters, such as @, # , $
# cannot contain the user name or parts of the user’s full name,
# such as their first name

# Use CSS to style headings, font, and form.
# Make sure your coding style complies with PEP 8


# EXTRA CREDIT
# Add additional form fields to build a more complex form
#   with additional options, such as city/state/country of residence,
#   favorite animal or hobby
# JavaScript is utilized for a date dropdown
# for the Date of Birth validation feature.
# JavaScript is utilized for text formatting for the
# Bio validation feature. (WYSIWYG)

# A password strength “meter” is displayed when validating passwords.

# FINAL TODO: Add an online image editor to the avatar.
# Include the basic functionality:
#   rotate,
#   crop and
#   flip.
# PNG mockup supplied.
