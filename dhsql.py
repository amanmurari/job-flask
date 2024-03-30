import sqlite3
engine= sqlite3.connect("job.db")
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
      
print(load_all())



def pagination(id):
    off = (id-1)*5
    conn.execute("SELECT * FROM job_list LIMIT "+str(off)+",5")
    rows = conn.fetchall()
    if len(rows) == 0:
      return None
    else:
      return rows
                                                  
                                                                                          
def apply(data):
    conn.execute( f"INSERT INTO User (name,email,job_id,linkdin_url,resume,password) VALUES ('{data['fullname']  }','{data['email']}',{data['job_id']},'{data['linkdin_url']}','{data['resume_url']}','{data['password']}')" )
    engine.commit()
    
    
    
    
def add_job(data):
  conn.execute(f'''
  INSERT INTO `job_list` (`job_title`, `job_location`, `salary`, `currency`, `company_name`, `responsibility`, `prerequisite`) 
  VALUES ('{data['job_title']}','{data['location']}',{data['salaey']},'{data['currency']}','{data['name']}','{data['responcibility']}','{data['prereqiisite']}'')
  
  ''')
  engine.commit()