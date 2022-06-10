
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from typing import List, Dict
import os
from PIL import Image
import base64
from io import BytesIO

class Routes:
    app = FastAPI()
    # CORS(app)

    def __init__(self):
        self.app.mount("/static", StaticFiles(directory="./static"), name="static")
        self.templates = Jinja2Templates(directory="templates")

    def run(self):
        print("Run Routes")
        self.start()
        return self.app

    def start(self):
        print("Start Routes")
        app = self.app
        templates = self.templates

        @app.get("/", response_class=HTMLResponse)
        async def index(request: Request):
            context = {"request": request}
            return templates.TemplateResponse("index.html", context)

        @app.get("/browse", response_class=HTMLResponse)
        async def browse(request: Request):
            context = {"request": request}
            return templates.TemplateResponse("browse.html", context)

        @app.get("/prediction", response_class=HTMLResponse)
        async def prediction(request: Request):
            context = {"request": request}
            return templates.TemplateResponse("prediction.html", context)

        @app.get("/type", response_class=HTMLResponse)
        async def type(request: Request):
            types = os.listdir('static/clothes/')
            number_of_types = len(types)
            print(types)
            context = {"request": request}
            context["types"] = types
            context["number_of_types"] = number_of_types
            return templates.TemplateResponse("type.html", context)

        @app.get("/camera", response_class=HTMLResponse)
        async def camera_get(request: Request):
            context = {"request": request}
            return templates.TemplateResponse("camera.html", context)

        @app.post("/camera_post", response_class=HTMLResponse)
        async def camera_post(file: UploadFile = File(...)):
            if not file:
                print("No image")
            else:
                #dataURL = bytes(image, 'utf-8')
                image = await file.read()
                with open("temp.jpg", "wb") as fh:
                    fh.write(image)

                #im = Image.open("temp.jpg")
                print("image is here")

            return templates.TemplateResponse("camera.html")

        @app.post("/upload")
        async def upload(image: UploadFile = File(...)):
            try:
                contents = await image.read()
                with open("uploaded_" + image.filename, "wb") as f:
                    f.write(contents)
            except Exception:
                return {"message": "There was an error uploading the file"}
            finally:
                await image.close()

            return {"message": f"Successfuly uploaded {image.filename}"}

