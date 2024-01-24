import requests

# payload = {'username': 'KOD', 'password': 'testing'}

r = requests.get('https://httpbin.org/basic-auth/KOD/testing', auth=('KOD', 'testing'))  # , data=payload)
print(r.text)
# print(r.content)
# with open('comic.png', 'wb') as f:
#    f.write(r.content)
# r_dict = r.json()
# print(r_dict['form'])
