"""
PyFileCleaner
Ferramenta para organizar arquivos por extensão.
"""

from pathlib import Path
from config_loader import load_rules
from organizer import get_destination_folder, move_file


DESTINATION_MAP = {
    "Images": Path.home() / "Imagens",
    "Videos": Path.home() / "Vídeos",
    "Documents": Path.home() / "Documentos",
    "Music": Path.home() / "Música",
    "Others": Path.home() / "Instalaveis",
}


def main():
    """
    Função principal do PyFileCleaner.
    """
    rules = load_rules("config/rules.json")

    source_dir = Path.home() / "Downloads"
    print(f"Organizando arquivos em: {source_dir}")

    if not source_dir.exists():
        print("Pasta Downloads não encontrada")
        return

    for item in source_dir.iterdir():
        if item.is_file():
            folder_name = get_destination_folder(item, rules)
            destination_dir = DESTINATION_MAP.get(folder_name)

            if destination_dir is None:
                print(f"Destino não configurado para {folder_name}")
                continue

            move_file(
                file_path=item,
                destination_dir=destination_dir,
                dry_run=False
            )


if __name__ == "__main__":
    main()
