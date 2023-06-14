import sqlite3

conn = sqlite3.connect('patient.db')

cur = conn.cursor()
#cur.execute("CREATE TABLE PATIENT_DETAILS(PATIENT_NAME VARCHAR(30),PATIENT_AGE INT,GENDER VARCHAR(10), DIABETIC VARCHAR(20))")
cur.execute("INSERT INTO PATIENT_DETAILS VALUES('MITHIL',26,'MALE','NEGITIVE')")
conn.commit()