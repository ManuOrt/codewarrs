import codewars_test as test


def search(budget, prices):
    respond = []
    lista_ordenada = sorted(prices)

    for num in lista_ordenada:
        if num <= budget:
            respond.append(num)

    converter = (str(item) for item in respond)
    return ','.join(converter)


if __name__ == "__main__":
    search(3, [6, 1, 2, 9, 2])
