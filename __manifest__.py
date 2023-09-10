{
    'name' : 'ROHaus',
    'version' : '1.0',
    'summary':'Haus Route Optimization ',
    'sequence':10,
    'description':"""Route Optimization Platform Haus""",
    'category':'Productivity',
    'website':'',
    'license': 'LGPL-3',
    'depends':[
        'sale',
        'mail',
        'website_slides',
        'board'
    ],
    'data':[
        'views/contents.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo':[],
    'qweb':[],
    'installable':True,
    'application':True,
    'auto_install':False,
    'css': [
    "static/src/css/custom.css",  # Path ke file CSS Anda
    ],
}