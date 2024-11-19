from backend.lineup_team.models import Player


class PlayerQueries:
    @staticmethod
    def exists_player_by_transfermarkt_url(transfermarkt_url: str) -> bool:
        exists_player = Player.objects.filter(transfermarkt_url=transfermarkt_url).exists()

        return exists_player

    @staticmethod
    def get_players_by_club_id(club_id: int) -> list[Player]:
        players = Player.objects.filter(club_id=club_id).all()

        return players
