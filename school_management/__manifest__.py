{
    'name': "School Management",
    'summary': "School Management Software",
    'description': "module to manage school",
    'author': "Bilal",
    'website': "http://www.schoolmanagement.com",
    'category': 'Extra Tools',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/school_bus.xml',
    ],
    'demo': [
        'demo/demo.xml',

    ],
}
