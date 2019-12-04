# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime

class Test(models.Model):
    _name = "test.test"
    _description = "Test"
    _rec_name ='name'


    name = fields.Char("Name")

