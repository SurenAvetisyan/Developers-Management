{
    'name': "developers_management",
    'description': """Developers""",
    'author': "Avetisyan",
    'category': 'Hidden',
    'version': '16.0.1.0.0',
    'depends': ['base'],

    # always loaded
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/developer.xml',
        'views/developer_menu.xml',
        'views/res_company.xml',
    ],
    "images": [
        "static/description/icon.png",
    ],
}
