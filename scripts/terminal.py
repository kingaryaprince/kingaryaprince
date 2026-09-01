"""Render the retro terminal GIF at the top of the profile README.

Uses github-readme-terminal (gifos) to simulate a shell session that prints a
neofetch-style panel over live GitHub stats. Needs ffmpeg on PATH and a
GITHUB_TOKEN with read access for the GraphQL stats query.

    python scripts/terminal.py

Writes output.gif into the working directory; the caller moves it to
assets/terminal.gif.

Note: the bundled gohufont-uni-14 is a latin-1 bitmap font, so every string
here has to stay inside ASCII. Block-drawing characters raise
UnicodeEncodeError at render time.
"""

import sys

import gifos

USER = "kingaryaprince"

BAR_WIDTH = 30
LABEL_WIDTH = 16  # must exceed len("pull requests") or the column collides

# 92 green, 93 yellow, 94 blue, 96 cyan, 95 magenta, 90 grey, 0 reset
G, Y, B, C, M, D, R = (
    "\x1b[92m", "\x1b[93m", "\x1b[94m", "\x1b[96m", "\x1b[95m", "\x1b[90m", "\x1b[0m",
)

FALLBACK_ROWS = [
    ("focus", "backends, on-device ML, real-time vision"),
    ("stack", "Python, TypeScript, Swift, Java, SQL"),
]
FALLBACK_LANGS = [("Python", 47.9), ("TypeScript", 47.2), ("Swift", 0.6)]


def fetch():
    """Return (stat_rows, languages). Falls back to static text if the API fails."""
    try:
        s = gifos.utils.fetch_github_stats(user_name=USER)
    except Exception as exc:  # network down, token missing, rate limited
        print(f"WARN: stats fetch failed ({exc}); using fallback", file=sys.stderr)
        return FALLBACK_ROWS, FALLBACK_LANGS

    if s is None:
        print("WARN: stats fetch returned None; using fallback", file=sys.stderr)
        return FALLBACK_ROWS, FALLBACK_LANGS

    rows = [
        ("commits", f"{s.total_commits_all_time} all time"
                    f"{D}  /  {R}{s.total_commits_last_year} in the last year"),
        ("pull requests", f"{s.total_pull_requests_made} opened"
                          f"{D}  /  {R}{s.total_pull_requests_merged} merged "
                          f"({s.pull_requests_merge_percentage:.0f}%)"),
    ]
    return rows, s.languages_sorted[:4]


def bar(pct):
    filled = round(BAR_WIDTH * pct / 100)
    return f"{G}{'#' * filled}{R}{D}{'.' * (BAR_WIDTH - filled)}{R}"


def main():
    t = gifos.Terminal(width=1000, height=430, xpad=16, ypad=14)
    t.set_fps(18)
    t.set_prompt(f"{G}arya{R}@{Y}berkeley{R}:{B}~{R}$ ")

    row = 1
    t.gen_text(f"{D}Last login: whenever the tests went green{R}", row)
    row += 2

    t.gen_prompt(row)
    t.gen_typing_text("whoami", row, contin=True, speed=2)
    row += 1
    t.gen_text("arya prince", row)
    t.gen_text(
        f"{D}b.a. data science + computer science, uc berkeley, may 2028{R}", row + 1
    )
    row += 3

    t.gen_prompt(row)
    t.gen_typing_text("gh stats --live", row, contin=True, speed=2)
    row += 1

    stat_rows, langs = fetch()
    panel = [f"{C}{USER}{R}@{Y}github{R}", f"{D}{'-' * (len(USER) + 7)}{R}"]
    for label, value in stat_rows:
        panel.append(f"{B}{label.ljust(LABEL_WIDTH)}{R}{value}")
    panel.append("")
    for name, pct in langs:
        panel.append(f"{B}{name.lower().ljust(LABEL_WIDTH)}{R}{bar(pct)} {pct:5.1f}%")
    panel.append(f"{D}{' ' * LABEL_WIDTH}public repos, by bytes{R}")

    t.gen_text(panel, row)
    row += len(panel) + 1

    t.gen_prompt(row)
    t.gen_typing_text("cat now.txt", row, contin=True, speed=2)
    row += 1
    t.gen_text(
        [
            f"{M}>{R} teaching CS 61A, 30+ students a week on interpreters and recursion",
            f"{M}>{R} building Relay: voice travel-recovery agent on an atomic Redis capture ledger",
        ],
        row,
    )
    row += 2

    t.gen_prompt(row)
    t.clone_frame(30)

    t.gen_gif()


if __name__ == "__main__":
    main()
