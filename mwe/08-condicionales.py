# Revisar si una condición se cumple
balance = 500
if balance > 0:
    print('Puedes pagar.')

balance = 0
if balance > 0:
    print('Puedes pagar.')
else:
    print('No tienes saldo')

# Likes
likes = 200
if likes == likes:
    print(f'Excelente, tienes {likes} likes.')

# IF con string
language = 'Python'
if language == 'Python':
    print(f'{language}: A truly fine choice.')

# IF con string
language = 'Java'
if not language == 'Python':
    print(f'{language}: not the expected choice.')

# Boolean
authenticated_user = True
if authenticated_user: # == True:
    print('System access granted.')
else:
    print('Please login.')

# Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']
if 'PHP' in lenguajes:
    print('PHP in list')
else:
    print('PHP not enlisted')

# IF anidados
user_authenticated = True
user_admin = True

if user_authenticated:
    if user_admin:
        print('Acceso total')
    else:
        print('Acceso al sistema')
else:
    print('Debe loguearse al sistema')