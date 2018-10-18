#_*_coding:utf-8_*_
#filename:main.py

import web

urls=(
    '/','index',
    '/dbdo','selectdo',
    '/add','adddata'
    )

db=web.database(dbn='mysql',host='localhost',port=3306,user='cstmzs',pw='112233',db='cstmzsfile')
render=web.template.render('templates/')

class index:
    def GET(self):
        i=web.input(name='hook')
        return render.index(i.name)

class selectdo:
    def GET(self):
        showname=db.select('muser')
        return render.showuser(showname)

class adddata:
    def POST(self):
        i=web.input()
        n=db.insert('muser',uname=i.uname,passw=i.passw)
        raise web.seeother('/dbdo')

    

if __name__=='__main__':
    app=web.application(urls,globals())
    app.run()
