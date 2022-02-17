import unittest

from app import documents, directories, add_new_doc, show_all_docs_info, check_document_existance, get_doc_owner_name, get_all_doc_owners_names, add_new_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf

class TestSomething(unittest.TestCase):

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance("2207 876234"), True)
        self.assertEqual(check_document_existance("234"), False)

    def test_get_doc_owner_name(self):
        number_pass = [
            "2207 876234",
            "11-2",
            "10006"
        ]
        test_name = [
            "Василий Гупкин",
            "Геннадий Покемонов",
            "Аристарх Павлов"
        ]
        for id, num in enumerate(number_pass):
            self.assertEqual(get_doc_owner_name(num), test_name[id])
    
    def test_get_all_doc_owners_names(self):
        list_user = []
        for el in documents:
            list_user.append(el['name'])
        self.assertEqual(get_all_doc_owners_names(), set(list_user))

    def test_add_new_shelf(self):
        test_case = ['1', '4', '5', '6', '12']
        for el in test_case:
            if el not in directories.keys():
                self.assertEqual(add_new_shelf(el), (el, True))
            else:
                self.assertEqual(add_new_shelf(el), (el, False))

    def test_delete_doc(self):
        test_case = [
            '123',
            '2207 876234',
            '11-2',
            '10006'
        ]
        nim = 0
        for el in test_case:
            for el_dict in documents:
                if el == el_dict['number']:
                    nim = 1
            if nim == 1:
                self.assertEqual(delete_doc(el), (el, True))
            else:
                self.assertEqual(delete_doc(el), (el, False))
    
    def test_get_doc_shelf(self):
        test_case = [
            "123",
            "2207 876234",
            "11-2",
            "10006"
        ]
        for el in test_case:
            doc_exist = check_document_existance(el)
            if doc_exist:
                for directory_number, directory_docs_list in directories.items():
                    if el in directory_docs_list:
                        self.assertEqual(get_doc_shelf(el), (el, directory_number))
            else:
                self.assertEqual(get_doc_shelf(el), (el, False))
    
    def test_move_doc_to_shelf(self):
        test_case_number = [
            "2207 876234",
            "11-2",
            "10006"
        ]
        test_case_shelf = ['1', '2', '3', '4', '5']
        for el_num in test_case_number:
            exist = check_document_existance(el_num)
            for el_shelf in test_case_shelf:
                if el_shelf in directories.keys():
                    if exist:
                        self.assertEqual(move_doc_to_shelf(el_num, el_shelf), (True, el_num, el_shelf))
                    else:
                        self.assertEqual(move_doc_to_shelf(el_num, el_shelf), (False, el_num, el_shelf))
                else:
                    self.assertEqual(move_doc_to_shelf(el_num, el_shelf), (False, el_num, el_shelf))

    def test_show_all_docs_info(self):
        list_test = []
        for el in documents:
            strings = f'"{el["type"]}" "{el["number"]}" "{el["name"]}"'
            list_test.append(strings)
        self.assertEqual(show_all_docs_info(), list_test)
    
    def test_add_new_doc(self):
        list_test = [
            {'new_doc_number': '123',
            'new_doc_type': 'pass',
            'new_doc_owner_name': 'daniil',
            'new_doc_shelf_number': '3',
            },
            {'new_doc_number': '678',
            'new_doc_type': 'snils',
            'new_doc_owner_name': 'dima',
            'new_doc_shelf_number': '6',
            },
            {'new_doc_number': '2207 876234',
            'new_doc_type': 'passport',
            'new_doc_owner_name': 'Василий Гупкин',
            'new_doc_shelf_number': '1',
            }
        ]
        for el in list_test:
            new_doc_number = el['new_doc_number']
            new_doc_type = el['new_doc_type']
            new_doc_owner_name = el['new_doc_owner_name']
            new_doc_shelf_number = el['new_doc_shelf_number']
            self.assertEqual(add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number), new_doc_shelf_number)