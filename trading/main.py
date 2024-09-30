from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return "Hello world"

@app.get("/bye/")
def bye_bye():
    return "Bye bye world"

@app.get("/bye1/")
def bye_bye1():
    return "Bye bye world"
