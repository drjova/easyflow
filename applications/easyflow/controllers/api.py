"""from gluon.tools import Service
service = Service()
import json
def call():
    return service()

@service.json
def addWorkflow(name,description):
    workflowID = db.workflow.insert(name=name,description=description)
    return dict(inserted=workflowID)
@service.json
def addStatus(workflowID,args):
	if workflow:
		args = json.loads(args)
		return dict(args=args)"""

@request.restful()
def workflow():
    response.view = 'generic.json'
    def GET(id):
        return dict(person = db.workflow(id))
    def POST(**fields):
        return db.workflow.validate_and_insert(**fields)
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