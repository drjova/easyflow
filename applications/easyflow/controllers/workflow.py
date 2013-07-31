# coding: utf8

def view_workflows():
    form = SQLFORM(db.workflow_types).process()
    if form.accepted:
        response.flash = 'new record inserted'
    records = SQLTABLE(db().select(db.workflow_types.ALL),headers='fieldname:capitalize')
    return dict(form=form, records=records)
