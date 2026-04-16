#!/usr/bin/env python3
# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_vault_security.py                              :+:     :+:    :+:    #
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


class ArchiveError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def extract_safely(fic: str) -> None:
    try:
        print("Initiating secure vault access...")
        with open(fic, "r", encoding="UTF-8") as f:
            print("Vault connection established with failsafe protocols\n")
            content: str = f.read()
            if (not content.strip()):
                raise ArchiveError("Empty file")
            print("RECOVERED DATA: ")
            print(content)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator firs.")
    except ArchiveError as e:
        print(f"ARCHIVE ERROR : {e}")
    except Exception as e:
        print(f"ANOMALY DETECTED: '{e}'")
    finally:
        print()


def secure_preservation(fic: str) -> None:

    def existing_file(fichier: str) -> int:
        try:
            fichier = open(fichier, "r", encoding="UTF-8")
            if fichier:
                fichier.close()
                raise FileExistsError(f"'{fic}' already exists")
        except FileExistsError as e:
            print(f"{RED}ARCHIVE PROTOCOL VIOLATION: {RESET}")
            print(f"{GREY}{ARROW}\tREASON: {e}{RESET}")
            print(f"{GREY}{ARROW}\tACTION: Overwrite prohibited \
to prevent data loss.{RESET}")
            print(f"{BLUE}-> Aborting operation...\n{RESET}")
            return 1
        except FileNotFoundError:
            return 0

    info: str = "[CLASSIFIED] New security protocols archived"
    if existing_file(fic):
        return None
    try:
        with open(fic, "w", encoding="UTF-8") as f:
            print("SECURE PRESERVATION:")
            print(info)
            f.write(info)
    except Exception as e:
        print(f"ANOMALY DETECTED: {e}")
    finally:
        print("Vault automatically sealed upon completion\n")


def ft_vault_security() -> None:
    file_to_open: str = "classified_data.txt"
    file_to_create: str = "security_protocols.txt"
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    extract_safely(file_to_open)
    secure_preservation(file_to_create)
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
