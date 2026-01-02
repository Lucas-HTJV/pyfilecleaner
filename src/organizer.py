"""
Responsável por analisar arquivos e decidir o destino com base nas regras.
"""

from pathlib import Path


def get_destination_folder(file_path: Path, rules: dict) -> str:
    """
    Retorna o nome da pasta de destino com base na extensão do arquivo.
    """
    extension = file_path.suffix.lower()

    for folder, extensions in rules.items():
        if extension in extensions:
            return folder

    return "Others"


def move_file(file_path: Path, destination_dir: Path, dry_run: bool = True):
    """
    Move o arquivo para o diretório de destino.
    Se dry_run=True, apenas simula a operação.
    """
    target_path = destination_dir / file_path.name

    if dry_run:
        print(f"[SIMULAÇÃO] {file_path.name} → {destination_dir.name}")
        return

    destination_dir.mkdir(parents=True, exist_ok=True)
    file_path.rename(target_path)
    print(f"[MOVIDO] {file_path.name} → {destination_dir.name}")
