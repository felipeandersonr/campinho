import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campinho.settings')
django.setup()

from loguru import logger

from lineup_team.controllers.club import ClubController
from lineup_team.controllers.transfermarkt import TransfermarktController


def load_clubs(data_clubs: list[dict]):
    logger.warning("creating clubs in db")

    for data_club in data_clubs:
        ClubController().create_club(data_club)


def data_load():
    bra1_transfermarkt_url = "https://www.transfermarkt.com/campeonato-brasileiro-serie-a/startseite/wettbewerb/BRA1"

    transfermarkt_controller = TransfermarktController()

    clubs = transfermarkt_controller.get_clubs_infos_by_competition_transfermarkt_url(
        competition_transfermarkt_url=bra1_transfermarkt_url
    )

    load_clubs(clubs)

    # depois adicionar a adicao de player by club.
    # acho que tem q existir um modelo de player_club_contract (jogador - club - season)


if __name__ == "__main__":
    data_load()
