# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Library',
    'version': '1.1',
    'summary': 'Library of school',
    'sequence': 1,
    'description': """ all data about screen library_module_new """,
    'category': 'assigment purpose',
    'depends': [],
    'data': [
        "security/ir.model.access.csv",
        "views/record_teacher.xml",
        "views/student_record_view.xml",
        "views/new_lib.xml"
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
