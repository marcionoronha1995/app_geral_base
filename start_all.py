import importlib.metadata
import pathlib
import subprocess
import sys

# Configurações de Identidade do Projeto
PROJECT_NAME = "App Geral Login - V8"
DEPENDENCIES = [
    "python-dotenv",
    "flask",
    "pandas",
    "openpyxl",
    "ruff",
    "jupyter_http_over_ws",
]


def run_step(description, command_list):
    """Executa um comando de sistema e reporta o status."""
    print(f"🔹 {description}...")
    try:
        subprocess.check_call(
            [sys.executable] + command_list, stdout=subprocess.DEVNULL
        )
        return True
    except Exception as e:
        print(f"❌ Falha em {description}: {e}")
        return False


def setup_environment():
    root = pathlib.Path(__file__).parent.resolve()

    print(f"--- 🚀 INICIALIZANDO {PROJECT_NAME} ---")

    # 1. Limpeza de Cache do PIP (Resolve os avisos de Deserialization)
    run_step("Limpando cache do instalador", ["-m", "pip", "cache", "purge"])

    # 2. Sincronização de Dependências
    missing = [d for d in DEPENDENCIES if not is_installed(d)]
    if missing:
        run_step(f"Instalando {missing}", ["-m", "pip", "install"] + missing)

    # 3. Sanitização do Sistema (Remoção de desktop.ini)
    try:
        from src.backend.core.secure_loader import cleanup_system_files

        cleanup_system_files()
    except ImportError:
        print("ℹ️ Módulo de limpeza não encontrado.")

    # 4. Abertura das Janelas de Serviço (PowerShell Externo)
    launch_services(root)


def is_installed(package):
    try:
        importlib.metadata.version(package)
        return True
    except importlib.metadata.PackageNotFoundError:
        return False


def launch_services(root):
    """Abre o Servidor Flask e o Jupyter para Colab em janelas separadas."""
    print("🖥️  Disparando serviços em janelas externas...")

    try:
        from colab_local_bridge import launch_colab_local_server
        from run_v8 import launch_server_external

        # Centraliza as chamadas usando as funções robustas já existentes
        launch_server_external()
        launch_colab_local_server()
    except ImportError as e:
        print(f"❌ Erro ao importar serviços externos: {e}")


if __name__ == "__main__":
    setup_environment()
    print("\n✅ AMBIENTE TOTALMENTE OPERACIONAL.")
