from marshmallow import fields, Schema


class DolarSchema(Schema):
    price = fields.Float(required=True)


class EuroSchema(DolarSchema):
    pass