# coding: utf8
from gluon.tools import Auth
auth = Auth(db, controller="home")
auth.define_tables()
from gluon.tools import Crud
crud = Crud(db)

db.define_table(
        'workflow',
        Field('id', ondelete='CASCADE'),
        Field('name', "string", default = None),
        Field('description', "string", default = None),
        Field('logo', "string", default = None),
        Field('user_id', db.auth_user, default = auth.user.id if auth.user else None, readable = False, writable = False),
        format = '%(name)s')

db.define_table(
        'status',
        Field('id'),
        Field('name', "string", default = None),
        Field('description', "string", default = None),
        Field('workflow_order', "integer", default = 1),
        Field('workflow_id', db.workflow),
        Field('user_id', db.auth_user, default = auth.user.id if auth.user else None, readable = False, writable = False),
        format = '%(name)s')

db.define_table(
        'detail',
        Field('id'),
        Field('name', "string", default = None),
        Field('description', "string", default = None),
        Field('status_order', "integer", default = 1),
        Field('status_id', db.status),
        Field('user_id', db.auth_user, default = auth.user.id if auth.user else None, readable = False, writable = False),
        format = '%(name)s')

db.define_table(
        'occurrence',
        Field('id'),
        Field('name', "string", default = None),
        Field('description', "string", default = None),
        Field('workflow_id', db.workflow),
        Field('status_id', db.status),
        Field('user_id', db.auth_user, default = auth.user.id if auth.user else None, readable = False, writable = False),
        Field('is_active', "boolean", default = True),
        format = '%(name)s')

db.define_table(
        'occurrence_detail',
        Field('occurrence_id', db.occurrence),
        Field('detail_id', db.detail),
        Field('detail_value', "string", default = None),
        format = '%(name)s')

db.workflow.name.requires = IS_NOT_EMPTY()
db.workflow.description.requires = IS_NOT_EMPTY()
