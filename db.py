import sqlite3
class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """ CREATE TABLE IF NOT EXISTS PetsRescue(ID integer primary key,
                                                      clinicname text,
                                                      doctorname text,
                                                      city text,
                                                      area text,
                                                      pagelink text,
                                                      mobile text,
                                                      address text)"""

        self.cur.execute(sql)
        self.con.commit()
    def insert (self,clinicname,doctorname,city,area,pagelink,mobile,address):
        self.cur.execute("insert into PetsRescue values(NULL,?,?,?,?,?,?,?)",
                         (clinicname,doctorname,city,area,pagelink,mobile,address))
        self.con.commit()
    def fetch (self):
        self.cur.execute("select * from PetsRescue")
        rows = self.cur.fetchall()
        return rows
    def remove(self,id):
        self.cur.execute("delete from PetsRescue where id=?",(id,))
        self.con.commit()
    def update(self,id,clinicname,doctorname,city,area,pagelink,mobile,address):
        self.cur.execute("update PetsRescue set clinicname=?,doctorname=?,city=?,area=?,pagelink=?,mobile=?,address=? where id=?",
                         (clinicname,doctorname,city,area,pagelink,mobile,address,id))
        self.con.commit()

    def search(self,clinicname="",doctorname="",combocity="",area="",pagelink="",mobile="",textaddress=""):
        self.con=sqlite3.connect("Petsrescue.db")
        self.cur=self.con.cursor()
        self.cur.execute("insert into PetsRescue values(NULL,?,?,?,?,?,?,?)",(clinicname,doctorname,combocity,area,pagelink,mobile,textaddress))
        self.con.commit()
        self.con.close()


