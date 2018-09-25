# -*- coding: utf-8 -*-
{
    'name': 'pos_customer_hide',
    'version': '1.0.0',
    'category': 'Point Of Sale',
    'author': 'ITSS',
    'sequence': 10,
    'summary': 'pos_customer_hide',
    'description': "",
    'depends': ['point_of_sale'],
    'data': [
        'views/header.xml'
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'license': 'OPL-1'
}
