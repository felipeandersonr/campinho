from django.http import JsonResponse

from backend.lineup_team.controllers.player import PlayerController


def lineup(request, club_id: int) -> JsonResponse:
    players = PlayerController().get_players_by_club_id(
        request=request,
        club_id=club_id
    )

    return players
