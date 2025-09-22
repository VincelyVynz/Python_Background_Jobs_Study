# ------------------------- Threading ------------------------- #
import threading
import time

def download_files(url):
    print(f"Starting download {url}")
    time.sleep(2)
    print(f"Download finished {url}")

t1 = threading.Thread(target=download_files, args = ("file_1",))
t2 = threading.Thread(target=download_files, args = ("file_2",))

t1.start()
t2.start()
t1.join()
t2.join()