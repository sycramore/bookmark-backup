# SPDX-License-Identifier: GPL-3.0-or-later

import os
import requests
from bs4 import BeautifulSoup

# Path to your local HTML file
html_file = "/home/sycramore/Schreibtisch/lesezeichen_backup/bookmarks_23.03.25.html"  # Example: "file:///Users/username/Desktop/page.html"

# Read the local HTML file
with open("/home/sycramore/Schreibtisch/lesezeichen_backup/bookmarks_23.03.25.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Create a directory for downloads
os.makedirs("downloads", exist_ok=True)

# Extract all links
links = [a["href"] for a in soup.find_all("a", href=True)]

print(f"Found {len(links)} links. Starting download...")

# Download each link
for i, link in enumerate(links):
    if not link.startswith("http"):
        print(f"Skipping non-http link: {link}")
        continue  # Skip local relative links

    try:
        file_name = os.path.basename(link) or f"file_{i}.html"
        response = requests.get(link)
        with open(f"downloads/{file_name}", "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    except Exception as e:
        print(f"Failed to download {link}: {e}")

print("All downloads completed!")
