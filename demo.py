from joytide import banner
from joytide import art
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
    section("confetti() demo")
    print("Launching colorful confetti animation… 🎉\n")
    confetti(width=60, height=15, n_particles=80, spawn_time=2.5)
    print("\nCongratulations!!\n")



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


def demo_alfardil() -> None:
    section("alfardil")
    print("todo")


def demo_omer() -> None:
    section("omer")
    print("todo")


def main() -> None:
    demo_banner()
    # uncomment your demo calls when ready to test
    # demo_confetti()
    demo_ascii_art()
    # demo_alfardil()
    # demo_omer()


if __name__ == "__main__":
    main()
