from django.http import JsonResponse

from lineup_team.controllers.club import ClubController


def get_clubs(request) -> JsonResponse:
    clubs = ClubController().get_clubs(request)

    return clubs
