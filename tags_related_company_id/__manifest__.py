# -*- coding: utf-8 -*-
{
    'name': "Primary Company Tag",

    'summary': """
    Primary company tag on contacts. Useful if company_id is too restrictive or you need customized reports.
    """,
    'description':"""
    1. Go to Settings -> Users and select the user you need to limit visible records
    2. Select 'Subject to access rights'
    3. Go to Contacts module and select a business contact with children records (Business + Individuals)
    4. You will see a new field below 'tags' where you can select which users can view this record.
    5. Access rights are inherited by children after applying
    Feel free to email me if you need any help: sbouillon@netfxtech.com
    """,

    'author': "NetFX Tech",
    'website': "https://netfxtech.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
    ],
}
