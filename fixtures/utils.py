
def check_key_exists(arr: list, element):
    """
    Метод для проверки принадлежности ключа к колонне
    :return Bool
    """
    for el in arr:
        if el in element or 'Empty' in element:
            return True
    return False


def check_fields(arr: list):
    """
    Метод для проверки пустых полей. Добавляет пустое поле, если такого нет
    :return Возвращает обработанный список
    """
    for t, el in enumerate(arr[:8]):
        if el.count(':') == 1:
            arr[t] = arr[t] + f' Empty_filed_{t}: null'
    return arr


def check_empty_values(arr: list, model):
    """
    Метод для обработки входящего списка.
    :param arr: массив с элементами строк
    :param model: модель данных
    :type model: Класс с данными
    :return Возвращает обработанный список
    """
    for elem in arr:
        for pos, el in enumerate(elem):
            if pos != len(elem) - 1:
                if el in model.exp_first_col and elem[pos+1] in model.exp_second_col:
                    elem.insert(pos+1, 'null')
    return arr


def list_processing(arr: list, model):
    """
    Метод для обработки входящего списка.
    :param arr: массив с элементами строк
    :param model: модель данных
    :type model: Класс с данными
    :return Возвращает обработанный список
    """
    unused_elem = [':', 'BY:', 'DATE:', 'SOURCE:']
    for k in model.exp_first_col:
        for pos2, elem in enumerate(arr):
            for pos, el in enumerate(elem):
                if ' ' in el:  # Стрип пробелов
                    arr[pos2][pos].lstrip()
                    arr[pos2][pos].rstrip()
                if el in unused_elem:  # Удаление ненужных элементов
                    del elem[pos]
                if k in el:  # Изменение названий ключей первой колонки
                    elem[pos] = k
                if 'NOTES' in el:  # Обработка значения для Qty
                    elem[pos] = el.replace('NOTES', '')
    for m in model.exp_second_col:  # Изменение названий ключей второй колонки
        for elem in arr:
            for pos, el in enumerate(elem):
                if m in el:
                    elem[pos] = m
    for pos2, elem in enumerate(arr):
        for pos, el in enumerate(elem):
            if ':' in el:
                elem[pos] = el.replace(':', '')

    return arr

