# coding: utf8
from gluon.tools import Service
service = Service()

def index():
  records = db(db.workflow.dataowner==auth.user_id).select()
  if len(records) > 0:
    records = records
  else:
    records = 'No records yet'
  return dict(title='Workflows',records=records,app='workflows')

def view():
     rows = db(db.workflow.dataowner==2).select()
     return dict(records=rows)

def start():
    workflowID = request.vars.workflowID
    if workflowID:
        response.flash = "New instance created!"
        return dict(record=workflowID,error=False,message='Workflow successfuly added!')
    else:
        return dict(record=workflowID,error=True,message='WorkflowID is empty!')
def delete():
    workflowID = request.vars.workflowID
    if workflowID:
        db(db.workflow.id == workflowID).delete()
        return dict(record=workflowID,error=False,message='Successfuly deleted!')
    else:
        return dict(record=workflowID,error=True,message='WorkflowID is empty!')
@service.json
def create(a):
    return dict(record=a)

def single():
   record = db.workflow(request.args(0)) or redirect(URL('view'))
   return dict(records=record)
def edit():
      return 'Hello'
def user(): return dict(form=auth())

#def index():
#redirect(URL('view'))
def call():
    session.forget()
    return service()
@auth.requires_login()
def details():
    form = SQLFORM.smartgrid(db.workflow)
    return dict(form=form)
def data(): 
  return dict(form=crud())

