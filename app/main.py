from fastapi import FastAPI, HTTPException
from pymemcache.client.base import Client
import hashlib
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uuid
from starlette_context import middleware, plugins, context
import os
from mangum import Mangum
from typing import Union



try:
    MEMCACHED_ADDR = os.environ['MEMCACHED_ADDR']
except:
    MEMCACHED_ADDR = 'localhost'

client = Client(MEMCACHED_ADDR)

app = FastAPI()
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    middleware.ContextMiddleware,
    plugins=(
        plugins.ForwardedForPlugin(),
    ),
)


@app.get("/api/create")
def create(site: str = 'global', key: Union[str, None] = None, value: int = 1):

    if key is None:
        key = str(uuid.uuid4().hex)
    key_hashed = hashlib.md5(key.encode() + site.encode()).hexdigest()
    client.set(key_hashed, str(value))
    return {
        "site": site,
        "key": key,
        "value": value
    }

@app.get("/api/get/{site}/{key}")
def get_value(site:str, key:str):
    key = key.encode() + site.encode()
    key = hashlib.md5(key).hexdigest()
    value = client.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return {"value": int(value)}


@app.get("/api/incr/{site}/{key}")
def set(key: str, site: str, amt: int = 1):
    if amt <= 0:
        raise HTTPException(status_code=400, detail="amt invalid")
    key = key.encode() + site.encode()
    key = hashlib.md5(key).hexdigest()
    value = client.get(key)
    if value is None:
        client.set(key, str(amt))
        return {"value": amt}
    value = int(value) + amt
    client.set(key, str(value))
    return {"value": int(value)}
    

@app.get("/api/decr/{site}/{key}")
def set(key: str, site: str, amt: int = 1):
    if amt <= 0:
        raise HTTPException(status_code=400, detail="amt invalid")
    key = key.encode() + site.encode()
    key = hashlib.md5(key).hexdigest()
    value = client.get(key)
    if value is None:
        client.set(key, str(amt))
        return {"value": -amt}
    value = int(value) - amt
    client.set(key, str(value))
    return {"value": int(value)}


@app.get("/")
async def root():
    return RedirectResponse("/docs")