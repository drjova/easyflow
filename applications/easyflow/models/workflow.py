# coding: utf8
from gluon.tools import Auth
auth = Auth(db, controller="home")
auth.define_tables()
from gluon.tools import Crud
crud = Crud(db)

db.define_table(
        'workflow',
        Field('id'),
        Field('name'),
        Field('description'),
        Field('dataowner', db.auth_user, default=auth.user.id if auth.user
        else None, writable=False, readable=False),
        format = '%(name)s')

db.define_table(
        'status',
        Field('id'),
        Field('name'),
        Field('description'),
        Field('order_to_workflow'),
        Field('workflow_id', db.workflow),
        Field('dataowner', db.auth_user, default=auth.user.id if auth.user
        else None, writable=False, readable=False),
        format = '%(name)s')

db.define_table(
        'details',
        Field('id'),
        Field('name'),
        Field('description'),
        Field('order_to_status'),
        Field('status_id', db.status),
        Field('dataowner', db.auth_user, default=auth.user.id if auth.user
        else None, writable=False, readable=False),
        format = '%(name)s')

db.define_table(
        'instances',
        Field('id'),
        Field('workflow_id', db.workflow),
        Field('active_status_id', db.status),
        format = '%(name)s')

db.define_table(
        'instances_details',
        Field('id'),
        Field('detail_id', db.details),
        Field('instance_id', db.instances),
        Field('instanceValue'),
        format = '%(name)s')

db.workflow.name.requires = IS_NOT_EMPTY()
db.workflow.description.requires = IS_NOT_EMPTY()
