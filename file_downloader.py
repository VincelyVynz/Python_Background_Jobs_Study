import requests

url = input('Enter URL: ')
image_name = url.split('/')[-1]
if image_name == "":
    image_name = url.split('/')[-2]



response = requests.get(url)
response.raise_for_status()

if response.status_code == 200:
    with open(f"downloads/{image_name}", "wb") as file:
        file.write(response.content)

else:
    print(response.status_code)