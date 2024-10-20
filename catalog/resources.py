from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import Device, Customer, Model, Type, Inventory, Location

class DevicelistResource(resources.ModelResource):
    """
        Import Device
    """

    hostname = Field(attribute='hostname', column_name='title')  # Changed from 'Hostname' to 'title'
    customer = Field(attribute='customer', column_name='customer')  # Keep 'customer' lowercase
    model = Field(attribute='model', column_name='model')  # Keep 'model' lowercase
    serialn = Field(attribute='serialn', column_name='serialn')  # Keep 'serialn' lowercase
    tag = Field(attribute='tag', column_name='tag')  # Keep 'tag' lowercase
    type = Field(attribute='type', column_name='type')  # Keep 'type' lowercase
    location = Field(attribute='location', column_name='location')  # Keep 'location' lowercase
    buydate = Field(attribute='buydate', column_name='buy_date')  # Changed from 'Buy date' to 'buy_date'
    status = Field(attribute='status_verbose', column_name='status')  # Keep 'status' lowercase
    substatus = Field(attribute='substatus_verbose', column_name='substatus')  # Keep 'substatus' lowercase
    warranty = Field(attribute='warranty', column_name='warranty')  # Keep 'warranty' lowercase
    cost = Field(attribute='cost', column_name='cost')  # Keep 'cost' lowercase

    class Meta:
        model = Device
        fields = (
            'hostname', 'customer', 'model', 'serialn', 'tag', 'type', 
            'location', 'buydate', 'status', 'substatus', 'warranty', 'cost',
        )
        exclude = ('id',)
        import_id_fields = (
            'hostname', 'customer', 'model', 'serialn', 'tag', 'type', 
            'location', 'buydate', 'status', 'substatus', 'warranty', 'cost',
        )


    def dehydrate_customer(self, device):
        return '%s' % (device.customer)


class AssettagResource(resources.ModelResource):
    """
       Import Asset tag and Serial Number
    """
    
    num = Field(attribute='num', column_name='AssetTag')
    snum = Field(attribute='snum', column_name='SN')

    class Meta:
        model = Inventory
        exclude = ('id',)
        import_id_fields = ('num', 'snum',)
