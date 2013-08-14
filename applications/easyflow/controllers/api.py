# track module changes
from gluon.custom_import import track_changes; track_changes(True)

from gluon import current
db = current.db
auth = current.auth

from workflows import *
@request.restful()
def workflow():
    response.view = 'generic.json'
    def GET():
        w = Workflow()
        return dict(workflows=w.get())
    def POST(**fields):
        return fields
    def PUT(**fields):
        return db.workflow.validate_and_insert(**fields)
    return locals()
def status():
    response.view = 'generic.json'
    def GET(id):
        return dict(person = db.status(id))
    def POST(**fields):
        return db.status.validate_and_insert(**fields)
    def PUT(**fields):
        return db.status.validate_and_insert(**fields)
    return locals()