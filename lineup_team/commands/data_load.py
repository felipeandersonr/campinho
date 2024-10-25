from lineup_team.controllers.transfermarkt import TransfermarktController


def data_load():

    bra1_transfermarkt_url = ""

    transfermarkt_controller = TransfermarktController()

    clubs = transfermarkt_controller.get_clubs_infos_by_competition_transfermarkt_url(
        competition_transfermarkt_url=bra1_transfermarkt_url
    )

    for club in clubs:
        # adicionar club no banco de dados se o club nao existir
        pass


    # depois adicionar a adicao de player by club.
    # acho que tem q existir um modelo de player_club_contract (jogador - club - season)
    