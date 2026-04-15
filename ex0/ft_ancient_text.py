# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_ancient_text.py                               :+:      :+:    :+:    #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/15 09:56:42 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/15 09:56:42 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

class ArchiveError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def ft_ancient_text(file: str = "") -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print(f"\nAccessing Storage Vault: {file}")
        with open(file, "r", encoding="UTF-8") as fic:
            print("Connection established...\n")
            content: str = fic.read()
            if (not content.strip()):
                raise ArchiveError("Empty file")
            print("RECOVERED DATA: ")
            print(content)
    except FileNotFoundError:
        print(f"ERROR: Storage vault not found. Run data generator first.")
    except ArchiveError as e:
        print(f"ARCHIVE ERROR : {e}")
    except Exception as e:
        print(f"ANOMALY DETECTED: '{e}'")
    finally:
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ancient_fragment: str = "ancient_fragment.txt"
    ft_ancient_text(ancient_fragment)