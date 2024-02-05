def exists_word(word, instance):
    lower_word = word.lower()
    result = []

    for e in instance.queue:
        occurrences = [
            {"linha": i + 1}
            for i, line in enumerate(e["linhas_do_arquivo"])
            if lower_word in line.lower()
        ]

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": e["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
