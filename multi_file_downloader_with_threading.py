import requests, threading

print_lock = threading.Lock()

def download_file(url):
    image_name = url.split('/')[-1]
    if image_name == "":
        image_name = url.split('/')[-2]
    image_name = image_name.split('?')[0]

    with print_lock:
        print(f'Download {image_name} started...')

    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == 200:
        with open(f"downloads/{image_name}", "wb") as file:
            file.write(response.content)
        with print_lock:
            print(f'Download {image_name} completed.')
    else:
        print(response.status_code)



def main():
    threads = []
    user_input = input('Enter URLs separated by a comma: ')
    urls = user_input.split(',')
    for url in urls:
        threads.append(threading.Thread(target=download_file, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()