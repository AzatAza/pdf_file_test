from PyPDF2 import PdfFileReader
import os
from fixtures.base_model import PageModel
from fixtures.utils import check_key_exists, list_processing, check_fields, check_empty_values

pdf_path = os.path.dirname(__file__)
filename = os.path.join(pdf_path, 'file.pdf')


class TestExtract:
    def test_extract_information(self):
        """
        Цель: Проверить наличие элементов в файле и их расположение:
        Шаги:
            1. Обработать файл в удобную для проверки форму
            2. Проверить наличие элементов
            3. Проверить правильность расположения элементов
        Приоритет: Medium
        """
        pm = PageModel()
        with open(filename, 'rb') as f:
            pdf = PdfFileReader(f)
            page_1 = pdf.getPage(0)
            txt = page_1.extract_text()
            income_list = txt.split('\n')
            income_list = check_fields(income_list)
            income_list = [el.split(' ') for el in income_list]
            income_list = list_processing(income_list[1:], pm)
            income_list = check_empty_values(income_list, pm)
            # .*?:\s.*?\s
        for elem in income_list:
            for pos, el in enumerate(elem):
                if pos < 2:
                    if check_key_exists(pm.exp_first_col, el) is True:
                        if el != elem[:-1]:
                            if elem[pos+1] not in pm.exp_second_col:
                                pm.act_first_col.update({el: elem[pos+1]})
                            else:
                                pm.act_first_col.update({el: None})

                else:
                    if check_key_exists(pm.exp_second_col, el) is True:
                        if el != elem[:-1]:
                            if elem[pos+1] not in pm.exp_first_col:
                                pm.act_second_col.update({el: elem[pos+1]})
                            else:
                                pm.act_second_col.update({el: None})

        pm.act_first_col['TAGGED'] = pm.act_first_col.popitem()
        pm.act_second_col.update({'NOTES': income_list[-1]})
        first_col, second_col = list(pm.act_first_col.keys()), list(pm.act_second_col.keys())
        for pos in range(len(first_col)):
            assert first_col[pos] == pm.exp_first_col[pos], f'Элемент {first_col[pos]} не на своем месте'  # 2 проверки, что есть такой элемент и позиция
        for pos in range(len(second_col)):
            assert pm.exp_second_col[pos] in second_col[pos], f'Элемент {second_col[pos]} не на своем месте'
