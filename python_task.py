import pandas as pd
import pickle
import numpy as np
import sqlalchemy as db

con = db.create_engine('postgresql://iti:iti@localhost/python_task')

model = pickle.load(open('model.pkl', 'rb'))
sepal_length = input("Please Enter The Length of sepal : ")
sepal_width = input("Please Enter The width of sepal : ")
petal_length = input("Please Enter The Length of Petal : ")
petal_width = input("Please Enter The width of Petal : ")


data = [[sepal_length, sepal_width, petal_length, petal_width]]

df = pd.DataFrame(data, columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
df['species'] = model.predict(df)

df.to_sql(name='iris',con=con, schema = 'public', if_exists = 'append', index = False)


