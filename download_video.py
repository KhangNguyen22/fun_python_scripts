from requests import get
url = input("Url please: ")
name = input("title of vid: ")+".mp4"
print('Downloading')
 
# download the url contents in binary format
r = get(url, stream=True)
print(r.status_code)
# open method to open a file on your system and write the contents
count = 0
with open(name, 'wb') as f:
    for chunk in r.iter_content(chunk_size = 256):
        count += 256
        print(count/1000000)
        f.write(chunk)