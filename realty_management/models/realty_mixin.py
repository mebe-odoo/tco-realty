from odoo import api, fields, models


MODEL_MAPPING = {
    'realty.property': 'property',
    'realty.tenancy': 'tenancy',
}


class RealtyMixin(models.AbstractModel):
    _name = 'realty.mixin'

    def action_open_portal(self):
        # Case 1: We can load a record defined in xml using its XML ID through the self.env.ref method
        #         In this case, we only do this when we trigger the method from the Tenancies,
        #         Since we already defined a URL action for the tenancies
        if self._name == 'realty.tenancy':
            action = self.env.ref('realty_management.tenancy_portal_url').read(['url', 'target', 'type'])[0]
            action['url'] += '/' + str(self.id)
            action['target'] = '_blank'
            return action
        # Case 2: We can directly return a URL action by passing a url that contains either property or tenancy
        #         plus the id of the record
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://portal.fake-agency.com/' + MODEL_MAPPING[self._name] + '/' + str(self.id),
            'target': '_blank'
        }