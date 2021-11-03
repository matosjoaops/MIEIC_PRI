import sys
import requests
from bs4 import BeautifulSoup

filename = "example.txt"
new_file_counter = 1

with open(filename) as file:
    for line in file:
        filtered_line = line.rstrip()
        r = requests.get("http://" + filtered_line)
        if r.status_code != 200:
            print("Failed to get HTML file!")
        else:
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            feed_items = soup.find_all("item")
            for item in feed_items:
                with open(f"files/feed_item_{new_file_counter}.html", "w") as new_file:
                    new_file.write(str(item))
                new_file_counter += 1

        