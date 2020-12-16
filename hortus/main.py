# 3rd-party
import config
import databases
from classifications.views import router as classifications_router
from db.base import database
from fastapi import FastAPI
from floras.views import router as floras_router

app = FastAPI(
    title="HORTUS",
    description="Tool to generate example forest garden layouts",
    version=config.settings.version,
    # The openapi schema is usually served from /openapi.json
    # You can change the url or disable it with openapi_url
    # Disabling this will also disable the docs
    # openapi_url=None,
    # Swagger UI: served at /docs.
    # You can set its URL with the parameter docs_url.
    # You can disable it by setting docs_url=None.
    # docs_url=None,
    # ReDoc: served at /redoc.
    # You can set its URL with the parameter redoc_url.
    # You can disable it by setting redoc_url=None.
    # docs_url="/docs",
    redoc_url=None,
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(
    floras_router,
    prefix="/api/v1/floras",
    tags=["floras"],
)
app.include_router(
    classifications_router,
    prefix="/api/v1/classifications",
    tags=["classifications"],
)


# app.include_router(
#    cars_router, prefix="/api/v1/cars", tags=["cars"],
# )
# app.include_router(
#    cars_router, prefix="/api/v2/cars", tags=["cars"],
# )
