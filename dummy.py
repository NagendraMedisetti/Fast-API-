# from fastapi import FastAPI


# app=FastAPI()

# @app.get("/")
# def hello_world():
#     return{"message": "hello world"}

# @app.get("/name/{a}")
# def hello_name(a:str):
#     return{"message": f"hello {a}"}



from fastapi import FastAPI
app=FastAPI()

@app.get("/name")
def name():
   return{"messsage":"hello this is name endpoint"}