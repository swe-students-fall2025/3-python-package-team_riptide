from joytide import banner
from joytide import art
from joytide import game_2048
from joytide import race
from joytide import confetti


def section(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def demo_banner() -> None:
    section("banner()")
    print(banner("team_riptide", border="#", padding=1, align="center"))
    print()
    print("left align, no padding:")
    print(banner("hello", border="*", padding=0, align="left"))
    print()
    print("right align, padding=2, multi-char border:")
    print(banner("joytide", border="><", padding=2, align="right"))


def demo_confetti() -> None:
    print(banner("Joytide Demo", border="💫", padding=2, align="center"))
    print("\nWelcome to the Joytide demo! Let's celebrate some terminal joy.\n")

    section("confetti() demo")
    print("Launching colorful confetti animation (default)… \n")
    confetti(width=60, height=15, n_particles=30, spawn_time=2.5)
    print("\n Congrates Confetti!\n")

    print("Now testing a slower gravity, longer celebration* \n")
    confetti(width=60, height=20, n_particles=100, spawn_time=5.0, gravity=0.015, wind=0.005)
    print("\n Slower gravity confetti done! 🎊\n")

    print("Also a *mini confetti burst* for small terminals\n")
    confetti(width=30, height=10, n_particles=20, spawn_time=1.0)
    print("\n Mini confetti burst complete!\n")



def demo_ascii_art() -> None:
    section("art() demo")
    print("large nature art")
    print("-----------------------------------")
    art("nature", "large")
    print()

    print("small animal art\n")
    print("-----------------------------------")
    art("animal", "small")
    print()

    print("small random art!")
    print("-----------------------------------")
    art()
    print()


def demo_race() -> None:
    section("race() demo")
    print("Quick race with parameters")
    print("-----------------------------------")
    race(["Mario", "Peach", "Yoshi"], width=100, delay=0.2)

    print("Quick race with defaults")
    print("-----------------------------------")
    race(["Mario", "Peach", "Yoshi"])


def demo_2048() -> None:
    section("2048")
    print("/" * 40 + "\n")
    print("[*] Default parameters: (size=4, prob=0.25, winning_tile=2048)\n")
    print("/" * 40 + "\n")
    game_2048()
    print("/" * 40 + "\n")
    print("[*] Quick game: (size = 2, prob = 1.0, winning_tile = 64)\n")
    print("/" * 40 + "\n")
    game_2048(size=2, prob=1.0, winning_tile=32)
    print("/" * 40 + "\n")
    print("[*] Long game: (size = 5, prob = 0.1, winning_tile = 4096)\n")
    print("/" * 40 + "\n")
    game_2048(size=5, prob=0.1, winning_tile=4096)


def main() -> None:
    demo_race()
    demo_banner()
    demo_confetti()
    demo_ascii_art()
    demo_2048()


if __name__ == "__main__":
    main()
