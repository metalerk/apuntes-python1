#    modulo.archivo      funcion
from helpers.utils import (
	login, login2
)
# from helpers.utils import login, login2
# import helpers.utils as h

user1 = {
	'username': 'pepito',
	'level': 'pro',
	'password': 'therealpepito', 
	'info': {
		'address': 'Sillicon Valley',
		'phone': '1234567890', # trailing comma
	}
}

user2 = {
	'username': 'pepito2',
	'level': 'noob',
	'password': 'therealpepito2', 
	'info': {
		'address': 'Sillicon Valley',
		'phone': '1234567890', # trailing comma
	}
}

is_pro = login2(user1)
print(is_pro) # True

is_pro = login2(user2)
print(is_pro) # False