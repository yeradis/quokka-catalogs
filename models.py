#!/usr/bin/env python
# -*- coding: utf-8 -*-

from quokka.core.db import db
from quokka.core.models import Content, Image


class Brand(Content):
    body = db.StringField(required=False)


class Item(object):
    code = db.StringField(max_length=255, required=True)
    sku = db.StringField(max_length=255, unique_with='code', required=True)
    dimensions = db.StringField(max_length=255, required=False)
    weight = db.DecimalField(min_value=None, max_value=None, force_string=False, precision=2, rounding='ROUND_HALF_UP',
                             required=False)
    body = db.StringField(required=False)
    price_value = db.DecimalField(min_value=None, max_value=None, force_string=False, precision=2,
                                  rounding='ROUND_HALF_UP', required=False)
    msrp_value = db.DecimalField(min_value=None, max_value=None, force_string=False, precision=2,
                                 rounding='ROUND_HALF_UP', required=False)
    brand = db.ReferenceField(Brand, reverse_delete_rule=db.DENY)

    meta = {
        'indexes': [
            {'fields': ['code'], 'unique': True,
             'sparse': True, 'types': False},
            {'fields': ['sku'], 'unique': True, 'unique_with': 'code',
             'sparse': True, 'types': False},

        ],
    }


class Product(Content, Item):
    images = db.ListField(
        db.ReferenceField(Image, reverse_delete_rule=db.DENY), default=[]
    )


class Catalog(Content, Item):
    products = db.ListField(
        db.ReferenceField(Product, reverse_delete_rule=db.DENY), default=[]
    )




