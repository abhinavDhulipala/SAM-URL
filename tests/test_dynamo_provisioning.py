import unittest
import boto_utils



class TestDynamoProvision(unittest.TestCase):
    def setUp(self) -> None:
        self.session = boto_utils.flask_profile
        self.dynamodb = boto_utils.dynamodb

    def test_migration(self):
        created_table = boto_utils.migration()
        self.assertEqual(created_table.name, boto_utils.table_name)


if __name__ == '__main__':
    unittest.main()
