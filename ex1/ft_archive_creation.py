#!/usr/bin/env python3
# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_archive_creation.py                            :+:     :+:    :+:    #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/15 09:56:42 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/15 09:56:42 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
GREY = "\033[90m"
ARROW = "\u21B3"
DATA = [
    "[ENTRY 001] New quantum algorithm discovered\n",
    "[ENTRY 002] Efficiency increased by 347%\n",
    "[ENTRY 003] Archived by Data Archivist trainee"
]


def existing_file(file_path: str) -> int:
    try:
        fic = open(file_path, "r", encoding="UTF-8")
        if fic:
            fic.close()
            raise FileExistsError(f"'{file_path}' already exists")
    except FileExistsError as e:
        print(f"{RED}ARCHIVE PROTOCOL VIOLATION: {RESET}")
        print(f"{GREY}{ARROW}\tREASON: {e}{RESET}")
        print(f"{GREY}{ARROW}\tACTION: Overwrite prohibited \
to prevent data loss.{RESET}")
        print(f"{BLUE}-> Aborting operation...\n{RESET}")
        return 1
    except FileNotFoundError:
        return 0


def ft_archive_creation(file_path: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    if existing_file(file_path):
        return None
    try:
        print(f"Initializing new storage unit: {file_path}")
        with open(file_path, "w", encoding="UTF-8") as fic:
            print("Storage unit created successfully...\n")
            line: str = ""
            print("Inscribing preservation data...")
            for line in DATA:
                print(line.strip())
                fic.write(line)
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_path}' ready for long-term preservation.")
    except Exception as e:
        print(f"ANOMALY DETECTED {e}")


if __name__ == "__main__":
    file_path: str = "new_discovery.txt"
    ft_archive_creation(file_path)
