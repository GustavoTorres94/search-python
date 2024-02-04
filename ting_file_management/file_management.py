import sys


def txt_importer(path_file):
    if not path_file[-4:] == ".txt":
        sys.stderr.write("Formato inválido")
    try:
        file = open(path_file, "r")
        to_list = [line.rstrip("\n") for line in file.readlines()]
        file.close()
        return to_list
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
