# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2009 Sharoon Thomas
#    Copyright (C) 2010-Today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name' : 'SMS Template',
    'version' : '1.1',
    'author' : '广西云会计财税服务有限公司',
    'website' : 'http://www.yunkuaiji.me',
    'category' : 'Marketing',
    "depends": ["base",
                "smsclient",
                "email_template"],
    'description': """
SMS Templating (simplified version of the original Power SMS by www.yunkuaiji.me).
==================================================================================

    **Technical note:** only the templating system of the original Power SMS by 云会计 was kept.
    """,
    'data': [
        #'wizard/sms_template_preview_view.xml',
        'sms_template_view.xml',
        #'res_partner_view.xml',
        'ir_actions_view.xml',
        #'wizard/mail_compose_message_view.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'images': ['images/1_sms_account.jpeg','images/2_sms_template.jpeg','images/3_sms.jpeg'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
