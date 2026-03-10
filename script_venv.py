#script que cria um ambiente virtual e instala as dependencias do projeto a partir de um arquivo requirements.txt
#parametro passado deve ser o diretorio do projeto onde o ambiente virtual sera criado e onde o arquivo requirements.txt esta localizado
import os
import subprocess
import sys


def criar_ambiente(diretorio_projeto):
    if not os.path.exists(diretorio_projeto):
        print("O diretorio informado nao existe")
        return

    venv_path = os.path.join(diretorio_projeto, "venv")

    if os.path.exists(venv_path):
        print("O ambiente virtual ja existe")
        return

    try:
        subprocess.run(["python", "-m", "venv", venv_path], check=True)
        print("Ambiente virtual criado com sucesso")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar o ambiente: {e}")


def instalar_dependencias(diretorio_projeto, requirements_file):
    if not os.path.exists(requirements_file):
        print("Arquivo requirements.txt nao encontrado")
        return

    pip_path = os.path.join(diretorio_projeto,"venv","Scripts","pip.exe")

    try:
        subprocess.run([pip_path, "install", "-r", requirements_file], check=True)
        print("Dependencias instaladas com sucesso")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar dependencias: {e}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python script_venv.py <diretorio_projeto>")
        return

    diretorio_projeto = sys.argv[1]

    requirements_file = os.path.join(diretorio_projeto, "requirements.txt")

    criar_ambiente(diretorio_projeto)
    instalar_dependencias(diretorio_projeto, requirements_file)


if __name__ == "__main__":
    main()