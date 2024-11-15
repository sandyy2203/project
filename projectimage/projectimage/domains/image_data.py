from mongoengine import fields, Document

class image_data(Document):
        
    image_path = fields.StringField()
    image_name = fields.StringField()
    