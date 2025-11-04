from joytide import banner
from joytide import art
from joytide import game_2048
from joytide import race


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


# placeholders teammates will fill in later
def demo_confetti() -> None:
    section("confetti() demo")
    print("todo")


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
    # uncomment your demo calls when ready to test
    # demo_confetti()
    demo_ascii_art()
    demo_2048()


if __name__ == "__main__":
    main()
