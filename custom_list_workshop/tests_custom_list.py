import unittest

from OOP.workshop_custom_list.custom_list import CustomList, CustomListException


class TestCustomList(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList('Simona', 'Nedeva', 30)

    def test_custom_list_initialize(self):
        my_custom_list = CustomList(1, 'Dean', 1.5)

        self.assertEqual(len(my_custom_list.sequence), 3)
        self.assertEqual(my_custom_list.sequence, [1, 'Dean', 1.5])

    def test_custom_list_append_should_return_custom_list(self):
        expected_result = self.my_custom_list.append('GO')
        expected = self.my_custom_list[-1]
        self.assertEqual('GO', expected)
        self.assertEqual(['Simona', 'Nedeva', 30, 'GO'], expected_result)

    def test_custom_list_remove_when_valid_idx_should_return_removed_value(self):
        actual_value = self.my_custom_list.remove(1)
        expected_value = 'Nedeva'

        self.assertEqual(actual_value, expected_value)
        self.assertNotIn(expected_value, self.my_custom_list)
        self.my_custom_list.insert(1, expected_value)

    def test_custom_list_remove_when_idx_out_of_range_raise(self):
        expected_string = 'Custom List does not found element on given index'
        with self.assertRaises(CustomListException) as context:
            idx = len(self.my_custom_list)
            self.my_custom_list.remove(idx)

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_string)

    def test_custom_list_remove_when_idx_is_not_int_raise(self):
        expected_string = 'Wrong type index, must be Integer'
        with self.assertRaises(CustomListException) as context:
            idx = '4'
            self.my_custom_list.remove(idx)

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_string)

    def test_custom_list_get_when_valid_idx_should_return_value(self):
        actual_value = self.my_custom_list.get(1)
        expected_value = 'Nedeva'

        self.assertEqual(actual_value, expected_value)
        self.assertIn(expected_value, self.my_custom_list)

    def test_custom_list_get_when_invalid_idx_raise(self):
        expected_string = 'Custom List does not found element on given index'
        with self.assertRaises(CustomListException) as context:
            idx = len(self.my_custom_list)
            self.my_custom_list.get(idx)

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_string)

    def test_custom_list_get_when_invalid_idx_type_raise(self):
        expected_string = 'Wrong type index, must be Integer'
        with self.assertRaises(CustomListException) as context:
            idx = '43'
            self.my_custom_list.get(idx)

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_string)

    def test_custom_list_extend_with_iterable_should_return_new_custom_list(self):
        test_list = {'VT': 10, 'Bulgaria': 100}
        expected_list = ['Simona', 'Nedeva', 30, 'VT', 'Bulgaria']
        actual_list = self.my_custom_list.extend(test_list)

        self.assertEqual(len(self.my_custom_list), 5)
        self.assertEqual(self.my_custom_list.sequence, expected_list)
        self.assertEqual(actual_list, expected_list)

    def test_custom_list_extend_when_given_not_iterable_raise(self):
        test_value_to_add = 100
        expected_string = 'Given value must be iterable'
        with self.assertRaises(CustomListException) as context:
            self.my_custom_list.extend(test_value_to_add)

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_string)

    def test_custom_list_insert_whenGiven_validIdxValue_should_addValueOnIdxAndReturnList(self):
        expected_list = ['Simona', 'Europe', 'Nedeva', 30]
        actual = self.my_custom_list.insert(1, 'Europe')

        self.assertEqual(expected_list[1], actual[1])
        self.assertEqual(expected_list, actual)

    def test_custom_list_insert_whenGiven_invalidIdx_should_raise(self):
        expected_string = 'Custom List does not found element on given index'
        with self.assertRaises(CustomListException) as context:
            index = len(self.my_custom_list.sequence) + 2
            self.my_custom_list.insert(index, 'Europe')

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_string)

    def test_custom_list_insert_whenGiven_invalidTypeIdx_should_raise(self):
        expected_string = 'Wrong type index, must be Integer'
        with self.assertRaises(CustomListException) as context:
            self.my_custom_list.insert('4', 'Europe')

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_string)

    def test_custom_list_pop_removes_last_value_and_returns_it(self):
        expected_value = 30
        expected_list = ['Simona', 'Nedeva']

        actual = self.my_custom_list.pop()
        self.assertEqual(actual, expected_value)
        self.assertEqual(self.my_custom_list.sequence, expected_list)

    def test_custom_list_pop_when_empty_should_raise(self):
        expected_message = 'you can not pop from empty list'
        test_list = CustomList()
        with self.assertRaises(CustomListException) as context:
            test_list.pop()

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_message)

    def test_custom_list_clear_removes_all_values(self):
        self.my_custom_list.clear()

        self.assertEqual(len(self.my_custom_list.sequence), 0)

    def test_custom_list_index_should_returns_idx_given_value(self):
        actual_idx = self.my_custom_list.index('Simona')
        actual_idx_1 = self.my_custom_list.index('Nedeva')

        self.assertEqual(0, actual_idx)
        self.assertEqual(1, actual_idx_1)

    def test_custom_list_index_when_given_value_not_in_raise(self):
        expected_message = 'Value not in list'
        with self.assertRaises(CustomListException) as context:
            self.my_custom_list.index('Dean')

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_message)

    def test_custom_list_count_returns_number_of_times_val_in(self):
        self.my_custom_list.append('Simona')
        actual = self.my_custom_list.count('Simona')
        self.assertEqual(2, actual)

    def test_custom_list_count_when_val_not_in_should_return_zero(self):
        self.my_custom_list.clear()
        actual = self.my_custom_list.count('Simona')
        self.assertEqual(0, actual)

    def test_custom_list_reverse(self):
        expected = [5, 4, 3, 2, 1]
        test_list = CustomList(1, 2, 3, 4, 5)
        test_list.reverse()
        self.assertEqual(expected, test_list.sequence)

    def test_custom_list_copy(self):
        expected = ['Simona', 'Nedeva', 30]
        copy_list = self.my_custom_list.copy()
        self.assertEqual(expected, copy_list.sequence)
        copy_list.append('Dean')
        self.assertEqual(copy_list.sequence, ['Simona', 'Nedeva', 30, 'Dean'])

    def test_custom_list_size_return_length(self):
        actual = self.my_custom_list.size()
        self.assertEqual(actual, 3)

    def test_custom_list_add_first_should_add_at_theBeginning(self):
        self.my_custom_list.add_first('Dean')
        self.assertEqual(self.my_custom_list.sequence[0], 'Dean')
        self.my_custom_list.add_first(1000)
        self.assertEqual(self.my_custom_list.sequence[0], 1000)

    def test_custom_list_dictionize_should_return_dictionary(self):
        expected = {'Simona': 'Nedeva', 30: ''}
        actual = self.my_custom_list.dictionize()

        self.assertTrue(type(actual) == type(expected))
        self.assertEqual(actual['Simona'], expected['Simona'])
        self.assertEqual(actual[30], expected[30])
        self.my_custom_list.clear()
        actual = self.my_custom_list.dictionize()
        self.assertEqual(actual, {})

    def test_custom_list_move_should_move_count_el_at_the_back(self):
        expected = [30, 'Simona', 'Nedeva']
        actual = self.my_custom_list.move(2)
        self.assertEqual(expected, actual)

    def test_custom_list_move_when_amount_invalid_type_should_raise(self):
        expected_message = 'Wrong type index, must be Integer'
        with self.assertRaises(CustomListException) as context:
            self.my_custom_list.move('2')

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), expected_message)

    def test_custom_list_sum_returns_the_sum_of_all_elements(self):
        expected = 42
        actual = self.my_custom_list.sum()
        self.assertEqual(actual, expected)

    def test_custom_list_overbound_returns_idx_biggest_value(self):
        actual_idx = self.my_custom_list.overbound()
        self.assertEqual(actual_idx, 2)

    def test_custom_list_underbound_returns_idx_smallest_value(self):
        self.my_custom_list.append('A')
        actual_idx = self.my_custom_list.underbound()
        self.assertEqual(actual_idx, 3)


if __name__ == '__main__':
    unittest.main()
