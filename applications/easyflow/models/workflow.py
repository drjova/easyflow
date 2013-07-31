# coding: utf8
db.define_table(
        'workflow_types',
        Field('id'),
        Field('name'),
        Field('description'),
        format = '%(name)s')
