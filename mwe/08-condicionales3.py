# Operators AND + OR
user_logged = True
user_admin = False
if user_logged and user_admin:
    print('Administrator')
elif user_logged:
    print('User logged in')
else:
    print('You must login')