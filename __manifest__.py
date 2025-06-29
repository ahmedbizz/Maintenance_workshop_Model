{
    'name': 'AIS WORKSHOP MANGMENT',
    'version': '1.0',
    'summary': 'Daily Work',
    'sequence': -1,
    'depends': ['base', 'mail', 'board'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/chanal.xml',
        # 'data/workshop.sendreceived.csv',
        'data/seqence_data.xml',
        'data/expirdata.xml',
        'data/ais_inv_sq.xml',
        'views/res_users_view.xml',
        'views/manu_view.xml',
        'views/workshop.xml',
        'views/ais_inventory_view.xml',
        'views/empolyee.xml',
        'views/dashbord.xml',
        'report/workshop_sendreceived_print_badge.xml',
        'report/confirm_spar.xml',
        'report/report.xml',
        'report/custom_header.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'assets': {

        'web.assets_qweb': [

        ],
        'web.assets_backend': [
            'AIS_WORKSHOP/static/src/css/ribbon.css',


        ],
    },
}
