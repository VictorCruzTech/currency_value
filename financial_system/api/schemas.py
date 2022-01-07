from marshmallow import fields, Schema


class BaseSchema(Schema):
    price = fields.Float(required=True)
    created = fields.Date()


class DolarSchema(BaseSchema):
    pass
    

class EuroSchema(BaseSchema):
    pass
