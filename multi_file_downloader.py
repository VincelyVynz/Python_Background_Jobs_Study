import requests

url_input = input('Enter URL separated by a comma: ')
url_list = url_input.split(",")
for url in url_list:
    image_name = url.split('/')[-1]
    if image_name == "":
        image_name = url.split('/')[-2]
    image_name = image_name.split('?')[0]

    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == 200:
        print(f"Download {image_name} started...")
        with open(f"downloads/{image_name}", "wb") as file:
            file.write(response.content)
        print(f"Download {image_name} completed.")


    else:
        print(response.status_code)