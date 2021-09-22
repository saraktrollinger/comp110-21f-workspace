"""Choose your own adventure project."""

__author__ = "730393060"

from random import randint
DANCEMAN: str = '\U0001F57A'
SUNNIES: str = '\U0001F60E'
HALO: str = '\U0001F607'
GUITAR: str = '\U0001F3B8'
PENCIL: str = '\u270F\uFE0F'
ROSE: str = '\U0001F339'
points: int = 0
player: str


def main() -> None:
    """The programs's entrypoint."""
    greet()
    points: int = 0
    game_choice: int = 1
    while game_choice == 1:
        hey_jude: str = "hey jude"
        question_one: str = input("1. Take a sad song and make it better: ")
        if question_one == hey_jude:
            print(f"Correct! { DANCEMAN }")
            points = points + 1
        else:
            no_points(points)
        print(f"You have { points } points!")
        let_it_be: str = "let it be"
        question_two: str = input("2. And when the night is cloudy there is still a light that shines on me: ")
        if question_two == let_it_be:
            print(f"Nice work! { DANCEMAN }")
            points = points + 1
        else:
            no_points(points)
        print(f"You have { points } points!")
        helter_skelter: str = "helter skelter"
        question_three: str = input("3. You may be a lover but you ain't no dancer: ")
        if question_three == helter_skelter:
            print(f"You guessed it! { DANCEMAN }")
            points = points + 1
        else:
            no_points(points)
        print(f"You have { points } points!")
        blackbird: str = "blackbird"
        question_four: str = input("4. Take these broken wings and learn to fly: ")
        if question_four == blackbird:
            print(f"That's right! { DANCEMAN }")
            points = points + 1
        else:
            no_points(points)
        print(f"You have { points } points!")
        print("Final question!")
        follow_the_sun: str = "i'll follow the sun"
        question_five: str = input("5. And now the time has come, and so my love I must go: ")
        if question_five == follow_the_sun:
            print(f"You guessed the correct answer! { DANCEMAN }")
            points = points + 1
        else:
            no_points(points)
        print(f"Thank you for playing! You earned { points } / 5 points!")
        if points < 2:
            print("You are not a true Beatles fan. Go listen to their music right now and improve your taste!")
        else:
            if points < 5:
                print("You are a mediocre fan! Keep up the good work!")
            else:
                print(f"You are a Beatles superfan! Incredible job! { SUNNIES }")
        print("Would you like to:")
        print("1. Play again!")
        print("2. Discover what Beatles song to listen to next!")
        print("3. Quit game.")
        game_choice: int = int(input("What would you like to do (1, 2, or 3)? "))
    if game_choice == 2:
        dice_roll(1, 2, 3, 4)
    if game_choice == 3:
        print("Game over. Play again soon!")


def no_points(x: int) -> int:
    points == x + 0
    print("I'm sorry, that's not correct.")
    print("Better luck next time!")
    return points


def dice_roll(w: int, x: int, y: int, z: int) -> int:
    game_choice: int = 2
    while game_choice == 2:
        dice: int = randint(1, 4)
        if dice == w:
            print(f"Listen to 'Baby, It's You!' { HALO }")
        else:
            if dice == x:
                print(f"Listen to 'While my Guitar Gently Weeps!' { GUITAR }")
            else:
                if dice == y:
                    print(f"Listen to 'Paperback Writer!' { PENCIL }")
                else:
                    print(f"Listen to 'Something!' { ROSE }")
        print("Press 2 to find another song. Press 3 to quit the game.")
        game_choice: int = int(input("What would you like to do? "))
        if game_choice == 3:
            print("Game over. Play again soon!")
    return game_choice


def greet() -> None:
    """Welcome to the game."""
    print("Welcome to 'Guess that Song - Beatles Edition!'")
    player: str = input("What is your name? ")
    print(f"Thank you for deciding to play, { player }! Let's see how big of a Beatles fan you really are!")
    print("Here are some instructions:")
    print("Step 1: You will be given a song lyric. You will then guess the song that those lyrics came from.")
    print("Step 2: If you guess correctly, you will be awarded 1 point. If you guess incorrectly, you will recieve 0 points.")
    print("Step 3: You will be presented with your current score before moving on to the next song lyric.")
    print("Be careful! Type your answers in all lowercase letters in order to win!")
    print(f"Let's get going, { player }!")


if __name__ == "__main__":
    main()