from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def ApplicationFactory() -> FastAPI:
    """Init App Factory FastAPI"""
    application = FastAPI()

    origins = ["*"]
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = ApplicationFactory()


@app.get("/")
def check_health():
    return {"OK": True}
