import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campinho.settings')
django.setup()

from loguru import logger

from lineup_team.controllers.club import ClubController
from lineup_team.controllers.transfermarkt import TransfermarktController
from lineup_team.controllers.player import PlayerController

from lineup_team.models import Club


def load_clubs(data_clubs: list[dict]):
    logger.warning("creating clubs in db")

    for data_club in data_clubs:
        club = ClubController().create_club(data_club)

        data_players = TransfermarktController().get_players_by_club_transfermarkt_url(
            club_transfermarkt_url=club.transfermarkt_url
        )

        load_player(
            club=club,
            data_players=data_players
        )


def load_player(data_players: list[dict], club: Club):
    logger.warning("creating players in db and relate to club")

    for data_player in data_players:
        player = PlayerController().create_player(
            club=club,
            data_player=data_player
        )


def data_load():
    bra1_transfermarkt_url = "https://www.transfermarkt.com/campeonato-brasileiro-serie-a/startseite/wettbewerb/BRA1"

    data_clubs = TransfermarktController().get_clubs_infos_by_competition_transfermarkt_url(
        competition_transfermarkt_url=bra1_transfermarkt_url
    )

    load_clubs(data_clubs)

if __name__ == "__main__":
    data_load()
