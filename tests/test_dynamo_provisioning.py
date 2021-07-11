import os
import sys
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import boto_utils
from constants import TABLE_NAME


class TestDynamoProvision(unittest.TestCase):
    def setUp(self) -> None:
        self.dynamodb = boto_utils.dynamodb

    def test_migration(self):
        created_table = boto_utils.migration()
        self.assertEqual(created_table.name, TABLE_NAME)


if __name__ == '__main__':
    unittest.main()
