"""EX06- Choose Your Own Adventure."""

__author__ = "730559522"

from random import randint
SHIELD = "\U000026E8"
BAT = "\U0001F987"
huge_boost: int = 100
small_boost: int = 20


def main() -> None:
    greet()
    global points
    supe_knowledge : bool = True
    while supe_knowledge:
        select: str = input(f" \n 1. See how much you enjoy comedy \n 2. See how much darkness you desire \n 3. Find more interest in superheroes \n: ")
        if select == "1": 
            supes_comedy()
        elif select == "2":
            points = dark(points)
        else:
            print(f"\n You are not a superhero fan. Gained superhero points: {points} \n Good bye {player}!")
            supe_knowledge = False

def greet() -> None:
    print("Welcome user! This game will determine whether you are a DC or Marvel person!")
    global player
    player = input("What's your name: ")


def supes_team() -> None:
    global points
    print("\n1. Consider what kinds of weapons you love using in combat\n2. Consider your favorite fighting style")
    consideration_combat: str = input(f"\n{player}, how will you prepare for combat")
    if consideration_combat == "1":
        points += huge_boost
        print(f"Start using a Captain America {SHIELD} to lead your team!")
    elif consideration_combat == "2":
        points += small_boost
        print(f"Fighting style is important, {player}, but weapons help more!")
def dark(player_darkness: int) -> int:
    if (): 

        return player_darkness

if __name__ == "__main__":
    main()