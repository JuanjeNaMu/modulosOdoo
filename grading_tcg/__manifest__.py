{
    'name': 'Grading TCG',
    'version': '1.0',
    'summary': 'Gestión de solicitudes de grading para cartas',
    'category': 'Services',
    'author': 'Juanje',
    'depends': ['base', 'contacts', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/grading_service_views.xml',
        'views/grading_request_views.xml',
        'views/grading_result_views.xml',
        'views/res_partner_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}