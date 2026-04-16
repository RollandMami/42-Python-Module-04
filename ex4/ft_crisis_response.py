#!/usr/bin/env python3
# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_crisis_response.py                             :+:     :+:    :+:    #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/15 09:56:42 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/15 09:56:42 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #


class EmpyDataError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class HeavyDataError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class HiddenScriptError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def sec_breach(fic: str) -> int:
    key_word: list = [
        b"sudo", b"rm -rf", b"DROP TABLE",
        b"<script>", b"import os", b"eval(",
        b"exec("]
    # test de la taille
    max_weight: int = 100 * 1024 * 1024
    with open(fic, "rb") as f:
        f.read(max_weight)
        if f.read(1):
            raise HeavyDataError("Potential breach detected, \
file weight > 100 Mo")
    with open(fic, "rb") as f:
        content: str = f.read()
        if b"\b" in content:
            raise HiddenScriptError("\\b detected")
        for word in key_word:
            if word in content:
                raise HiddenScriptError(f"Potential hidden script '{word}'")
    return 0


def safe_open(fic: str, heading: list = [], mode: int = 0) -> str:
    CDG = "UTF-8"
    try:
        print(f"{heading[mode][0]} Attempting access to '{fic}'...")
        sec_breach(fic)
        with open(fic, "r", encoding=CDG) as f:
            content = f.read()
            if (not content.strip()):
                raise EmpyDataError("Missing data")
            if (not sec_breach(fic)):
                print(f"{heading[mode][1]} Archive recovered - ``{content}''")
        return ("Normal operations resumed\n")
    # corrupted file
    except UnicodeDecodeError as e:
        print(f"{heading[mode][1]} Archive corupted error > {e}")
        return ("\n")
    except FileNotFoundError:
        print(f"{heading[mode][1]} Archive not found in storage matrix")
        return ("Crisis handled, system stable\n")
    except PermissionError:
        print(f"{heading[mode][1]} Security protocols deny access")
        return ("Crisis handled, security maintained\n")
    except EmpyDataError as e:
        print(f"{heading[mode][1]} {e}")
        return ("\n")
    except HeavyDataError as e:
        print(f"{heading[mode][1]} {e}")
        return ("\n")
    except HiddenScriptError as e:
        print(f"{heading[mode][1]} {e}")
        return ("\n")
    except Exception as e:
        print(f"{heading[mode][1]} {e}")
        return ("Crisis handled, security maintained\n")


def ft_crisis_response() -> None:
    file_names: list = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt",
        "corupted_archive.txt",
        "access_denied.txt",
        "security_protocols.txt"
        ]
    headings: list = [
        ["CRISIS ALERT:", "RESPONSE:"],
        ["ROUTINE ACCESS:", "SUCCESS:"],
    ]
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print(f"STATUS: {safe_open(file_names[0], headings, 0)}")
    print(f"STATUS: {safe_open(file_names[1], headings, 0)}")
    print(f"STATUS: {safe_open(file_names[2], headings, 0)}")
    # EXTRA TEST
    print(f"STATUS: {safe_open(file_names[4], headings, 1)}")
    print(f"STATUS: {safe_open(file_names[5], headings, 1)}")
    print("All crisis scenarios handled successfully. Archives secure")


if __name__ == "__main__":
    ft_crisis_response()
