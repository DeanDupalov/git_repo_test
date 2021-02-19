import unittest

from OOP.workshop_hash_table.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def test_HashTable_add(self):
        test_table = HashTable()
        test_table.add('tim', 'TestValue')

    def test_HashTableGet_whenKeyIsIn(self):
        expected = 'TestValue'
        test_table = HashTable()
        test_table.add('tim', 'TestValue')
        value = test_table.get('tim')
        self.assertEqual(expected, value)

    def test_HashTableGet_whenKeyIsNotPresent(self):
        expected = None
        test_table = HashTable()
        test_table.add('tim', 'TestValue')
        value = test_table.get('InvalidKeyTest')
        self.assertEqual(expected, value)




if __name__ == '__main__':
    unittest.main()
