# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (c) 2013 OpenERP S.A. <http://www.openerp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv


class actions_server(osv.Model):
    """ Add sms option in server actions. """
    _name = 'ir.actions.server'
    _inherit = ['ir.actions.server']

    def _get_states(self, cr, uid, context=None):
        res = super(actions_server, self)._get_states(cr, uid, context=context)
        res.insert(0, ('sms', 'Send Sms'))
        return res

    _columns = {
        'sms_from': fields.related(
            'sms_template_id', 'sms_from', type='char',
            readonly=True, string='From'
        ),
        'sms_to': fields.related(
            'sms_template_id', 'sms_to', type='char',
            readonly=True, string='To (sms)'
        ),
        #'partner_to': fields.related(
         #   'sms_template_id', 'partner_to', type='char',
         #   readonly=True, string='To (Partners)'
       # ),
       # 'subject': fields.related(
       #     'sms_template_id', 'subject', type='char',
       #     readonly=True, string='Subject'
        #),
        'body_html': fields.related(
            'sms_template_id', 'body_html', type='text',
            readonly=True, string='Body'
        ),
        'sms_template_id': fields.many2one(
            'sms.template', 'sms Template', ondelete='set null',
            domain="[('model_id', '=', model_id)]",
        ),
    }

    def on_change_sms_template_id(self, cr, uid, ids, sms_template_id, context=None):
        """ Render the raw template in the server action fields. """
        fields = ['sms_to']
        if sms_template_id:
            template_values = self.pool.get('sms.template').read(cr, uid, sms_template_id, fields, context)
            values = dict((field, template_values[field]) for field in fields if template_values.get(field))
            #if not values.get('sms_from'):
            #    return {'warning': {'title': 'Incomplete template', 'message': 'Your template should define sms_from'}, 'value': values}
        else:
            values = dict.fromkeys(fields, False)

        return {'value': values}

    def run_action_sms(self, cr, uid, action, eval_context=None, context=None):
        if not action.sms_template_id or not context.get('active_id'):
            return False
        self.pool['sms.template'].send_sms(cr, uid, action.sms_template_id.id, context.get('active_id'),
                                              force_send=False, raise_exception=False, context=context)
        return False


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
