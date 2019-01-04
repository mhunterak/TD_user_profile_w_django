'''
MASTER TODO LIST for User Profile project
'''
#TODO: Use the supplied HTML/CSS to build and style the profile page and bio page.

#TODO: Create a Django model for the user profile.
#TODO: Add routes to display a profile, edit a profile, and change the password.

#TODO: Create a “profile” view to display a user profile with the following fields: First Name, Last Name, Email, Date of Birth, Bio and Avatar. Include a link to edit the profile.
#TODO: Create an “edit” view with the route “/profile/edit” that allows the user to edit the user profile with the following fields: First Name, Last Name, Email, Date of Birth, Confirm Email, Bio and Avatar.

#TODO: Validate user input "Date of Birth" field: check for a proper date format (YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY)
#TODO: Validate user input "Email" field: check that the email addresses match and are in a valid format.
#TODO: Validate user input "Bio" field: check that the bio is 10 characters or longer and properly escapes HTML formatting.

#TODO: Add the ability to upload and save a user’s avatar image.

#TODO: Create “change-password” view with the route “/profile/change_password” that allows the user to update their password using User.set_password() and then User.save(). Form fields will be: current password, new password, confirm password
##TODO: Validate user input "Password" fields: check that the old password is correct using User.check_password() and the new password matches the confirm password field and follows the following password policy.
##TODO: must not be the same as the current password minimum password length of 14 characters.
##TODO: must use of both uppercase and lowercase letters must include one or more numerical digits must include one or more of special characters, such as @, #, $ cannot contain the user name or parts of the user’s full name, such as their first name

#TODO: Use CSS to style headings, font, and form.
#TODO: Make sure your coding style complies with PEP 8.

