from odoo.tests.common import TransactionCase


class TestDeveloper(TransactionCase):
    def setUp(self):
        super(TestDeveloper, self).setUp()
        self.Developer = self.env['developer']
        self.Company = self.env['res.company']

    def test_create_developer(self):
        # Create a developer record and test if it's created successfully
        company_data = {
            'name': 'ABC Company',
        }

        company = self.Company.create(company_data)

        developer_data = {
            'name': 'John Doe',
            'type': 'backend',
            'phone': '123-456-789',
            'email': 'johndoe@developers.com',
            'address': '123 Main St',
            'date_of_birth': '1990-01-01',
            'company_id': company.id,
        }
        developer = self.Developer.create(developer_data)
        self.assertEqual(developer.name, 'John Doe', "Developer not created")
