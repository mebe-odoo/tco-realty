from odoo.http import Controller, route, request


class RealtyController(Controller):

    @route('/property/<int:property_id>', auth='user', website=True, type='http')
    def property_page(self, property_id, **kwargs):
        record = request.env['realty.property'].browse(property_id)
        return request.render('realty_management.property_page', qcontext={'property_id': record})
