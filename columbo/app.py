#!/usr/bin/env python3

"""
Logging, arguments parser & actions router implementations.
"""

import subprocess

def main() -> None:
    """
    Main entry point of the application.
    """

    lines = subprocess.check_output(
        [
            "git",
            "log",
            "--since=1.day.ago",
            "--name-only",
            "--author=",
            "--no-renames",
            "--pretty=format:'%an'",
        ],
        encoding="utf-8",
    ).splitlines()

    author = ""
    authors = {}

    for line in lines:
        if line.strip() == "":
            continue

        is_author = line.startswith("'")

        if is_author and authors.get(line) is None:
            author = line
            authors[author] = []
            continue

        if not is_author:
            authors[author].append(line)

    for author in authors:
        authors[author] = list(set(authors[author]))
        authors[author].sort()

        print(author)
        for file in authors[author]:
            print(file)
        print()
