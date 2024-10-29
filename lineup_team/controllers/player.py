from loguru import logger

from lineup_team.models import Player, Club
from lineup_team.queries.player import PlayerQueries


class PlayerController:
    @staticmethod
    def create_player(data_player: dict, club: Club) -> Player | None:
        exists_player = PlayerQueries().exists_player_by_transfermarkt_url(data_player["transfermarkt_url"])

        if exists_player:
            return None

        new_player = Player.objects.create(
            club=club,
            name=data_player["name"],
            shirt_number=data_player["shirt_number"],
            transfermarkt_url=data_player["transfermarkt_url"]
        )

        logger.info(f"created player {new_player.name} - {new_player.transfermarkt_url}")

        return new_player
