import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page_url = "https://www.transfermarkt.com/corinthians-sao-paulo/startseite/verein/199/saison_id/2023"

response = requests.get(page_url, headers=headers)

page_bs = BeautifulSoup(response.content, "html.parser")

table_items = page_bs.find("table", {"class": "items"})
body_items = table_items.find("tbody")
player_rows = body_items.find_all("tr", recursive=False)

for player_row in player_rows:
    player_number = player_row.find("td").find("div").text

    player_content = player_row.find("table", {"class": "inline-table"})
    player_image_tag = player_content.find("img")
    player_image = player_image_tag.attrs["data-src"]
    player_name = player_content.find("a").text.strip()

    print("-=-=-" * 15)
    print(f"NAME = {player_name}")
    print(f"SHIRT NUMBER = {player_number}")
    print(f"IMAGE = {player_image}")
