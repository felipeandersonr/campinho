from loguru import logger

from campinho.settings import SCRAPING_BASE_URL
from lineup_team.controllers.club import ClubController
from lineup_team.controllers.transfermarkt import TransfermarktController
from lineup_team.controllers.player import PlayerController

from lineup_team.models import Club


def load_clubs(data_clubs: list[dict]):
    logger.warning("creating clubs in DB")

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
    logger.warning("creating players in DB and relating to club")

    for data_player in data_players:
        player = PlayerController().create_player(
            club=club,
            data_player=data_player
        )


def run():
    logger.info("starting data load...")

    data_clubs = TransfermarktController().get_clubs_infos_by_competition_transfermarkt_url(
        competition_transfermarkt_url=SCRAPING_BASE_URL
    )

    load_clubs(data_clubs)
