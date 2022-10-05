"""EX06- Choose Your Own Adventure."""

__author__ = "730559522"

from random import randint

SHIELD = "\U000026E8"
BAT = "\U0001F987"
player: str = ""
points: int = 0
huge_boost: int = 100
small_boost: int = 20
sad_childhood_measure: int = randint(50, 70)
social_isolation_measure: int = randint(75, 100)


def main() -> None:
    """Main function propels the program."""
    greet()
    global points
    supe_knowledge: bool = True
    while supe_knowledge:
        print(f"{player}'s total points: {points}")
        select: str = input(f" \n 1. See how much you care about tactics. \n 2. See how much darkness you desire for intimidation {BAT}. \n 3. Find more interest in superheroes \n: ")
        if select == "1": 
            supes_tactic()
        elif select == "2":
            points = dark(points)
        elif select == "3":
            print(f"\n You are not a superhero fan. Gained superhero points: {points} \n Good bye {player}!")
            supe_knowledge = False


def greet() -> None:
    """Greet function greets player and offers game background."""
    print("Welcome user! This game will determine what superhero you are!")
    global player
    player = input("What's your name: ")


def supes_tactic() -> None:
    """Supes tactic function asks player the combat method they prefer."""
    global points
    print("\n1. Consider what kinds of weapons you love using in combat\n2. Consider your favorite fighting style")
    consideration_combat: str = input(f"\n{player}, how will you prepare for combat: ")
    if consideration_combat == "1":
        points += huge_boost
        print(f"Start using a Captain America {SHIELD} to lead your team!")
    elif consideration_combat == "2":
        points += small_boost
        print(f"Fighting style is important, {player}, learn some Spider-Man moves!")


def dark(player_darkness: int) -> int:
    """The dark function examines how dark the player in question is."""
    global sad_childhood_measure
    global social_isolation_measure
    if (player_darkness <= 100): 
        sad_childhood_measure = randint(50, 70)
        player_darkness += small_boost
        print(f"You resemble a fairly dark superhero, the brainwahsed {player}! Yes, yourself! Oh lord!")
        return player_darkness
    else:
        social_isolation_measure = randint(75, 100)
        player_darkness += huge_boost
        print(f"You resemble an extremely serioius and dark superhero, the {BAT} man!")
        return player_darkness


if __name__ == "__main__":
    main()