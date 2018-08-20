def login(user):
	if user['level'] == 'pro':
		return True

	else:
		return False

def login2(user):
	return True if user['level'] == 'pro' else False