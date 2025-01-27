from django.db import models

# Create your models here.
# When you create a custom user model by subclassing AbstractUser (like your CustomUser model), the auth_user table is no longer used by Django for storing user data. Instead, Django will use the table corresponding to your custom model (e.g., CustomUser), which you defined.

# Here’s a breakdown of how things work:

# What Happens When You Create a Custom User Model?
# New User Table: When you create a custom user model and run the migrations, Django creates a new table for your custom model. This table will contain both the default fields from AbstractUser (like username, password, email, etc.) and any custom fields you’ve added (like phone, address, date_of_birth, etc.).

# So, if you defined a custom model CustomUser, Django will create a table (likely named myapp_customuser unless you specify a different table name in the Meta class).

# Old auth_user Table: The default auth_user table is only used by Django when you don't provide a custom user model and rely on the built-in User model. If you choose to use CustomUser, Django will no longer use the auth_user table.

# Important: When you switch to a custom user model in Django (via AUTH_USER_MODEL in settings.py), the auth_user table will not be used anymore, even for newly created applications. Your database will rely solely on the custom model (CustomUser in your case) for user data.

# Why Keep the auth_user Table?
# No impact on existing projects: If you're starting a project with a custom user model, then the auth_user table won't be used. However, if you’re switching from the default User model to a custom one (i.e., you added CustomUser after starting the project), there may be migration issues where Django’s migration system tries to keep the auth_user table for backward compatibility.

# Legacy or backward compatibility: The auth_user table is there for projects that have been using the default User model and have already migrated to it. For projects that are migrating to a custom user model after initial development, Django keeps the auth_user table to handle data migrations and ensure smooth transitions.

# Key Points to Remember:
# After migration: When you use a custom user model, Django uses the custom model’s table (e.g., CustomUser table) instead of auth_user.

# auth_user is the default table used for the built-in User model. If you want to use a custom user model, make sure to set AUTH_USER_MODEL in settings.py and run the migrations correctly.

# No interference: As long as you create the custom user model correctly before running migrations, Django will handle it without interference from auth_user.

# Migration issues: If you change the user model after running migrations with the default User, you’ll need to handle database migrations carefully to avoid conflicts between auth_user and your custom model.

# Example of What You Need in settings.py:
# To make sure Django uses your CustomUser model instead of the default User model, add the following line in your settings.py:

# python
# Copy
# Edit
# AUTH_USER_MODEL = 'myapp.CustomUser'  # Replace 'myapp' with your app name
# Once you’ve done this, Django will use the CustomUser model and its corresponding table instead of auth_user.

# Let me know if you need any more clarification on this!