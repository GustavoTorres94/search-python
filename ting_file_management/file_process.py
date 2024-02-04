import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_name = path_file.split("/")
    if any(
        entry["nome_do_arquivo"].split("/") == file_name
        for entry in instance.queue
    ):
        return

    file_content = txt_importer(path_file)
    dist_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }
    instance.enqueue(dist_file)

    print(dist_file)


def remove(instance):
    if not instance:
        return print("Não há elementos")
    else:
        removed = instance.search(0)["nome_do_arquivo"]
        instance.dequeue()
        return print(f"Arquivo {removed} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance.queue):
        sys.stderr.write("Posição inválida")
    else:
        return print(instance.search(position))
