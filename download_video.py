from requests import get
url = 'https://apse2.nv.instructuremedia.com/fetch/QkFoYkIxc0hhUU9TbFZWcEExUnlRbXdyQjFMYVFGOD0tLTI1NTdhYWM4MWE2MTE3ZWYwOTFhZGIzZmU2MzNhMWU0ODdhZTUzY2M.mp4'
print('Downloading')
 
# download the url contents in binary format
r = get(url, stream=True)
print(r.status_code)
# open method to open a file on your system and write the contents
count = 0
with open('t1.mp4', 'wb') as f:
    for chunk in r.iter_content(chunk_size = 256):
        count += 256
        print(count/1000000)
        f.write(chunk)