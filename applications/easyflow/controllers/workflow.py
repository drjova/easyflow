# coding: utf8

service = Service()

def index():
  records = db(db.workflow.dataowner==auth.user_id).select()
  if len(records) > 0:
    records = records
  else:
    records = 'No records yet'
  
  return dict(title='Workflows',records=records,app='workflows')


@auth.requires_login()
def create():
    form = SQLFORM(db.workflow).process()
    if form.accepted:
        response.flash = 'new record inserted'
    return dict(form=form)


def view():
     records = db(db.workflow.dataowner==2).select()
     return dict(records=records)


def single():
   record = db.workflow(request.args(0)) or redirect(URL('view'))

  
   return dict(records=record)
def edit():
      return 'Hello'
def user(): return dict(form=auth())

#def index():
#redirect(URL('view'))

@auth.requires_login()
def details():
    form = SQLFORM.smartgrid(db.workflow)
    return dict(form=form)
def data(): 
  return dict(form=crud())

