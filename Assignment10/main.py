from game_data import GameData
from service import Service
from ui import UI


def main():
    game_data = GameData()
    service = Service(game_data)
    ui = UI(service, game_data)
    ui.execute()


if __name__ == "__main__":
    main()
