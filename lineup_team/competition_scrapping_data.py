# import requests
# from bs4 import BeautifulSoup
#
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
#
# base_url = "https://www.transfermarkt.com"
#
# page_url = base_url + "/campeonato-brasileiro-serie-a/startseite/wettbewerb/BRA1"
#
# response = requests.get(page_url, headers=headers)
#
# page_bs = BeautifulSoup(response.content, "html.parser")
#
# table_items = page_bs.find("table", {"class": "items"})
# body_items = table_items.find("tbody")
# table_rows = body_items.find_all("tr", recursive=False)
#
# for table_row in table_rows:
#     club_name = table_row.find("a").attrs["title"]
#     detailed_club_url = table_row.find("a").attrs["href"]
#
#     detailed_club_url = base_url + detailed_club_url
#
#     detailed_club_response = requests.get(detailed_club_url, headers=headers)
#
#     soup = BeautifulSoup(detailed_club_response.content, "html.parser")
#
#     image_profile_container = soup.find("div", {"class": "data-header__profile-container"})
#
#     club_image = image_profile_container.find("img").attrs["src"]
#
#     print("-=-=-" * 15)
#     print(f"NAME = {club_name}")
#     print(f"IMAGE = {club_image}")
