import webbrowser
from time import sleep

url = input("Enter the URL : ")

while True:
    print("Refreshing...")
    webbrowser.open(url, new=0)
    sleep(3)
