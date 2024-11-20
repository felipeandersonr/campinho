from django.http import JsonResponse
from loguru import logger

from lineup_team.models import Club
from lineup_team.queries.club import ClubQueries


class ClubController:
    @staticmethod
    def create_club(club_data: dict) -> Club | None:
        club_transfermarkt_url = club_data["transfermarkt_club_url"]

        exists_club = ClubQueries().exists_club_by_transfermarkt_url(
            club_transfermarkt_url=club_transfermarkt_url
        )

        if exists_club:
            logger.error(f"already exists club {club_data['name']}")

            return None

        new_club = Club.objects.create(
            name=club_data["name"],
            transfermarkt_image_url=club_data["image"],
            transfermarkt_url = club_data["transfermarkt_club_url"],
        )

        logger.info(f"created club {club_data['name']} -- {club_transfermarkt_url}")

        return new_club

    @classmethod
    def get_clubs(cls, request) -> JsonResponse:
        clubs = ClubQueries().get_clubs()

        data = [
            {
                "id": club.id,
                "name": club.name,
                "image": club.transfermarkt_image_url,
                "transfermarkt_url": club.transfermarkt_url
            }

            for club in clubs
        ]

        response = JsonResponse(data=data, safe=False)

        return response
