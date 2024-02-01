import xmlrpc.client

url =  "http://localhost:8069"
db = "odooform"
username = "mohamed.touabti@weasydoo.com"
password = "mohamed"

common =xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
ver= common.version()

print(ver)
uid = common.authenticate(db,username,password,{})
print(uid)
if uid:
    print(True)
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    #NOTE: search records
    search_key='mohamed'
    res_rec = models.execute_kw(db, uid, password, 'voyage', 'search_read', [[['name', '=', search_key]]],
                                {'fields': ['id', 'name', 'montant']})
    for nb,rec in enumerate(res_rec):
        print("record_search_{}:{}".format(nb+1,rec))
    # NOTE: create records
    vals={'name':'TestCREATEexternalapi','montant':456.8,'voyageur_id':3}
    res = models.execute_kw(db, uid, password, 'voyage', 'create',[vals])
    print(res)
    search_key='TestCREATEexternalapi'
    res_rec=models.execute_kw(db,uid,password,'voyage','search_read',[[['name','=',search_key]]],{'fields':['id','name','montant']})
    for nb,rec in enumerate(res_rec):
        print("record_search_{}:{}".format(nb+1,rec))
else:
    print(False)


