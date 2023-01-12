import deployment.requests as requests
""" response = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
print(response.status_code)

if response.status_code == 200:
   print('Success!')
   #print(response.content)
   with open(r'img.png','wb') as f:
      f.write(response.content)

elif response.status_code == 404:
   print('Not Found.') """
response = requests.get('https://api.github.com')
print(response.status_code)

if response.status_code == 200:
   print('Success!')
elif response.status_code == 404:
   print('Not Found.')
