"""
Responsável por carregar as regras de organização do arquivo JSON.
"""

import json
from pathlib import Path


def load_rules(config_path: str) -> dict:
    """
    Carrega as regras de organização a partir de um arquivo JSON.
    """

    # Diretório raiz do projeto (um nível acima de /src)
    base_dir = Path(__file__).resolve().parent.parent

    # Caminho absoluto para o arquivo de configuração
    full_path = base_dir / config_path

    if not full_path.exists():
        raise FileNotFoundError(
            f"Arquivo de configuração não encontrado: {full_path}"
        )

    with full_path.open(encoding="utf-8") as file:
        return json.load(file)
