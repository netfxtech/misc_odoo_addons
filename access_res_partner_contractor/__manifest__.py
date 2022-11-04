# -*- coding: utf-8 -*-
{
    'name': "Access Rights - res.partner - Contractors",

    'summary': """
        Access rights on contacts based off tags linked to res.users.""",
    'description': """
    1. Go to settings -> Users -> Enable "Subject to access rights" on the user who should not be able to see all records.
    2. Go to any company record and you will see a new field called "Access Rights" on the contact.
    3. Select the users that can view this particular record + children records
    * Access rights are chosen on records who do not have a parent themselves (typically a business) -
      or an individual who is not associated to a company contact.
    """,

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
