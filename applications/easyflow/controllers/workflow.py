# coding: utf8

service = Service()

@auth.requires_login()
def index():
  records = db(db.workflow.dataowner==auth.user_id).select()
  if len(records) > 0:
    records = records
  else:
    records = 'No records yet'
  templateFile = os.path.join(paths.get_prog_root(), 'templates', 'view.html')
  return dict(title='Workflows',records=records,app='workflows',tem=templateFile)


@auth.requires_login()
def create():
    form = SQLFORM(db.workflow).process()
    if form.accepted:
        response.flash = 'new record inserted'
    return dict(form=form)

@auth.requires_login()
def view():
     records = db(db.workflow.dataowner==auth.user_id).select()
     return dict(records=records)

@auth.requires_login()
def single():
   record = db.workflow(request.args(0)) or redirect(URL('view'))
   form = SQLFORM(db.workflow, record)
   if form.process().accepted:
       response.flash = 'form accepted'
   elif form.errors:
       response.flash = 'form has errors'
   return dict(form=form)
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

