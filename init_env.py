import importlib.metadata
import os
import pathlib
import subprocess
import sys

# Lista de dependências essenciais para o seu projeto
REQUIREMENTS = [
    "python-dotenv",
    "flask",
    "pandas",
    "openpyxl",
    "ruff",
    "jupyter_http_over_ws",
]


def detect_environment():
    """Detecta onde o código está rodando."""
    if "COLAB_RELEASE_TAG" in os.environ:
        return "COLAB"
    if "PYTHONANYWHERE_DOMAIN" in os.environ:
        return "PYTHONANYWHERE"
    return "LOCAL"


def install_missing_dependencies():
    """Verifica e instala bibliotecas faltantes usando importlib (Padrão Python 3.14)."""
    missing = []
    for x in REQUIREMENTS:
        try:
            importlib.metadata.version(x)
        except importlib.metadata.PackageNotFoundError:
            missing.append(x)

    if missing:
        print(f"📦 Bibliotecas faltantes: {', '.join(missing)}")
        print("Wait... Sincronizando ambiente...")
        try:
            # sys.executable garante o uso do seu .venv
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
            print("✅ Sincronização concluída.")
        except Exception as e:
            print(f"❌ Erro na instalação: {e}")
    else:
        print("💎 Ambiente 100% atualizado.")


def verify_essentials():
    """Garante segurança e limpeza."""
    root = pathlib.Path(__file__).parent.resolve()

    # Verificação do .env
    if not (root / ".env").exists():
        print("⚠️ Criando .env base...")
        with open(root / ".env", "w") as f:
            f.write("SECRET_KEY=chave_v8_local\nDEBUG=True\n")

    # Executa a limpeza profissional de arquivos desktop.ini
    try:
        from src.backend.core.secure_loader import cleanup_system_files

        cleanup_system_files()
    except ImportError:
        print("ℹ️ Módulo secure_loader aguardando configuração.")


if __name__ == "__main__":
    print(f"🖥️  Sistema: {detect_environment()} | Python: {sys.version.split()[0]}")

    install_missing_dependencies()
    verify_essentials()

    print("\n🚀 PROJETO PRONTO PARA CODAR.")
