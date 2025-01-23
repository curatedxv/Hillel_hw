from pyexpat.errors import messages
from typing import Annotated
import random
import json
import string
import aiofiles
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def root(request: Request, long_url: Annotated[str, Form()]):
    short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    async with aiofiles.open("urls.json", "r") as f:
        urls = json.loads(await f.read())

    async with aiofiles.open("urls.json", "w") as f:
        urls[short_url] = long_url
        await f.write(json.dumps(urls))
    return {"message": f"ShortenUrl is {short_url}"}

@app.get("/{short_url}")
async def convert(short_url: str):
    async with aiofiles.open("urls.json", "r") as f:
        urls = json.loads(await f.read())
    if short_url in urls:
        return RedirectResponse(urls[short_url])
    else:
        raise HTTPException(status_code=404, detail="Item not found")
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}