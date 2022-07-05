# -*- coding: utf-8 -*-
# © 2018-Today Aktiv Software (http://www.aktivsoftware.com).
# Part of AktivSoftware See LICENSE file for full copyright
# and licensing details.

# Author: Aktiv Software.
# mail:   odoo@aktivsoftware.com
# Copyright (C) 2015-Present Aktiv Software PVT. LTD.
# Contributions:
#           Aktiv Software:
#              - Mital Parmar
#              - Yash Shah
#              - Tanvi Gajera
#              - Harshil Soni

{
    "name": "Pos Discount Limitation",
    "author": "Aktiv",
    "website": "http://www.aktivsoftware.com",
    "summary": """
        Restrict users when applying Discount.
        """,
    "description": """
        Title: Pos Discount Limitation \n
        Author: Aktiv Software \n
        mail: odoo@aktivsoftware.com \n
        Copyright (C) 2015-Present Aktiv Software PVT. LTD.
        """,
    "contributors": "Aktiv Software",
    # Categories can be used to filter modules in modules listing
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["pos_discount"],
    "license": "LGPL-3",
    # assets
    "assets": {
        "web.assets_common": ["pos_discount_limitation/static/src/js/discount.js"]
    },
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/point_of_sale_data.xml",
        "views/pos_discount_view.xml",
    ],
    "images": ["static/description/banner.jpg"],
    "installable": True,
    "application": True,
    "auto_install": False,
}
