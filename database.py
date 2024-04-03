import mysql.connector
import time
class DataBase:
  def __init__(self,user='root', password='root',host='127.0.0.1',database='flask',port=3306):
    while True:
      try:
        self.engine = mysql.connector.connect(user=user, password=password,host=host,database=database,port=port)
        self.conn=self.engine.cursor()
        break;
      except Exception as error:
        time.sleep(5)
        print('Error',error)
        
        
  def load_all():
     s = "select * FROM job_list"
     return self.conn.execute(s)
     
  def find_job(id):
     s = "select * FROM job_list WHERE job_id = "+str(id)
     s=self.conn.execute(s).fetchall()
     rows = s
     if len(rows) == 0:
       return None
     else:
      return rows
      
  def pagination(id):
    off = (id-1)*5
    result = self.conn.execute("SELECT * FROM job_list LIMIT "+str(off)+",5")
    rows = result.fetchall()
    if len(rows) == 0:
      return None
    else:
      return rows
  def apply(data):
    result = self.conn.execute( f"INSERT INTO User (name,email,job_id,linkdin_url,resume,password) VALUES ({random.randint(1,10000000000)},'{data['fullname']  }','{data['email']}',{data['job_id']},'{data['linkdin_url']}','{data['resume_url']}','{data['password']}')" )
    self.conn.commit()
                            
db=DataBase()
engine= sqlite3.connect("job.db",check_same_thread=False)
conn=engine.cursor()



def load_all():
     s = "select * FROM job_list"
     conn.execute(s)
     return conn.fetchall()
     


def find_job(id):
     s = "select * FROM job_list WHERE job_id = "+str(id)
     conn.execute(s)
     rows=conn.fetchall()
     if len(rows) == 0:
       return None
     else:
      return rows
      




def pagination(id):
    off = (id-1)*5
    conn.execute("SELECT * FROM job_list LIMIT "+str(off)+",5")
    rows = conn.fetchall()
    if len(rows) == 0:
      return None
    else:
      return rows
                                                  
                                                                                          
def apply(data):
    conn.execute( f"INSERT INTO User (id,name,email,job_id,linkdin_url,resume,password) VALUES ({random.randint(1,10000000000)},{data['fullname']  }','{data['email']}',{data['job_id']},'{data['linkdin_url']}','{data['resume_url']}','{data['password']}')" )
    engine.commit()
#self.engine.close()
