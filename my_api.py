import requests
import sqlalchemy as db
import pandas as pd
import json

api_key  = "e3c0d09979ad476686ca082aadf6706c"

url    = "https://api.spoonacular.com/recipes/complexSearch"

params = {
    "apiKey":   api_key,
}


response = requests.get(url, params=params)
print("Status code:", response.status_code)

df = pd.DataFrame.from_dict(response.json())
df['results_json'] = df['results'].apply(json.dumps)
df = df.drop(columns=['results'])

engine = db.create_engine('sqlite:///data_base_name.db')

df.to_sql('results', con=engine, if_exists='replace', index=False)



with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM results;")).fetchall()
   print(pd.DataFrame(query_result))