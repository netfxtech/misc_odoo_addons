# -*- coding: utf-8 -*-
{
    'name': "Access Rights - res.partner - Contractors",

    'summary': """
        Access rights on contacts based off tags linked to res.users.""",

    'author': "NetFX Tech",
    'website': "https://netfxtech.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security_groups.xml',
        'views/res_partner_views.xml',
        'views/res_users_views.xml',
    ],
}
