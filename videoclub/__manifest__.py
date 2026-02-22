{
    'name': "VideoclubSGE",
    'summary': "Gestión de películas de videoclub",
    'description': """
        Módulo para gestionar un videoclub:
        - Películas
        - Actores
        - Directores
        - Préstamos
    """,
    'author': "Juan Jesús",
    'website': "https://github.com/JuanjeNaMu/modulosOdoo/tree/main/videoclub",
    'category': 'Entertainment',
    'version': '1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/videoclub.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}