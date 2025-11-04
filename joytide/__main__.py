# joytide/__main__.py
import argparse

from .core import banner
from .core import art


def _run_banner(args) -> int:
    print(banner(args.text, border=args.border, padding=args.padding, align=args.align))
    return 0

def _run_art(args):
    art(theme=args.theme, size=args.size)
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="joytide", description="joytide CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # banner function
    p_banner = sub.add_parser("banner", help="print an ASCII banner")
    p_banner.add_argument("text")
    p_banner.add_argument("--border", default="*", help="border characters")
    p_banner.add_argument("--padding", type=int, default=1, help="spaces around text")
    p_banner.add_argument(
        "--align", choices=["left", "center", "right"], default="center"
    )
    p_banner.set_defaults(func=_run_banner)

    # art function
    p_art = sub.add_parser("art", help="print ASCII art")
    p_art.add_argument(
        "--theme", choices=["animal", "nature", "tech", "random"], default="random",
        help="theme of the art"
    )
    p_art.add_argument(
        "--size", choices=["small", "large"], default="small", help="size of the art"
    )
    p_art.set_defaults(func=_run_art)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
