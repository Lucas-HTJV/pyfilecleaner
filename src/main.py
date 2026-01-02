"""
PyFileCleaner
Ferramenta para organizar arquivos por extensão.
"""

from pathlib import Path
from config_loader import load_rules, load_config
from organizer import get_destination_folder, move_file


def main():
    rules = load_rules("config/rules.json")
    config = load_config("config/config.json")

    source_dir = Path.home() / config["source_dir"]
    dry_run = config.get("dry_run", True)

    destinations = {
        key: Path.home() / value
        for key, value in config["destinations"].items()
    }

    print(f"Organizando arquivos em: {source_dir}")

    if not source_dir.exists():
        print("Pasta de origem não encontrada.")
        return

    files_found = False

    for item in source_dir.iterdir():
        if item.is_file():
            files_found = True
            folder_name = get_destination_folder(item, rules)
            destination_dir = destinations.get(folder_name)

            if destination_dir is None:
                print(f"Destino não configurado para {folder_name}")
                continue

            move_file(
                file_path=item,
                destination_dir=destination_dir,
                dry_run=dry_run
            )

    if not files_found:
        print("Sem arquivos na pasta, tudo limpo ✅")


if __name__ == "__main__":
    main()
