from fastapi import FastAPI


def ApplicationFactory() -> FastAPI:
    """Init App Factory FastAPI"""
    application = FastAPI()

    return application


app = ApplicationFactory()


@app.get("/")
def check_health():
    return {"OK": True}
