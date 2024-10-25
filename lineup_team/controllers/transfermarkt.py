import requests
from bs4 import BeautifulSoup


class TransfermarktController:
    base_transfermarkt_url = "https://www.transfermarkt.com"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    }

    def get_clubs_infos_by_competition_transfermarkt_url(self,
                                                         competition_transfermarkt_url: str,
                                                         headers: dict | None = None) -> list[dict]:

        clubs = []

        if not headers:
            headers = self.headers

        response = requests.get(competition_transfermarkt_url, headers=headers)

        page_bs = BeautifulSoup(response.content, "html.parser")

        table_items = page_bs.find("table", {"class": "items"})
        body_items = table_items.find("tbody")
        table_rows = body_items.find_all("tr", recursive=False)

        for table_row in table_rows:
            club_name = table_row.find("a").attrs["title"]
            detailed_club_url = table_row.find("a").attrs["href"]

            detailed_club_url = self.base_transfermarkt_url + detailed_club_url

            detailed_club_response = requests.get(detailed_club_url, headers=headers)

            soup = BeautifulSoup(detailed_club_response.content, "html.parser")

            image_profile_container = soup.find("div", {"class": "data-header__profile-container"})

            club_image = image_profile_container.find("img").attrs["src"]

            club_info = {
                "name": club_name,
                "image": club_image,
                "transfermarkt_club_url": detailed_club_url
            }

            clubs.append(club_info)

        return clubs

    def get_players_by_club_transfermarkt_url(self,
                                              club_transfermarkt_url: str,
                                              headers: dict | None = None) -> list[dict]:

        players = []

        if not headers:
            headers = self.headers

        response = requests.get(club_transfermarkt_url, headers=headers)

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

            player_info = {
                "name": player_name,
                "image": player_image,
                "shirt_number": player_number
            }

            players.append(player_info)

        return players
