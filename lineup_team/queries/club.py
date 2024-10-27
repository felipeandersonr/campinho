from lineup_team.models import Club


class ClubQueries:
    @staticmethod
    def exists_club_by_transfermarkt_url(club_transfermarkt_url: str) -> bool:
        exists_club = Club.objects.filter(transfermarkt_url=club_transfermarkt_url).exists()

        return exists_club
