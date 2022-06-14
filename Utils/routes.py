
from unittest import TextTestResult
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
from Utils.prediction_model import prediction as pred_model
import uuid

class Routes:
    app = FastAPI()
    # CORS(app)

    def __init__(self):
        self.app.mount("/static", StaticFiles(directory="./static"), name="static")
        self.app.mount("/data", StaticFiles(directory="./data"), name="data")
        self.templates = Jinja2Templates(directory="templates")

    def check_folders(self):
        self.uploadfolder = "./data/uploaded/"
        self.userfolder = "./data/user/"
        self.moderatorfolder = "./data/moderator/"
        self.modelfolder = "./data/model/"
        if not os.path.exists(self.uploadfolder):
            os.makedirs(self.uploadfolder)
        if not os.path.exists(self.userfolder):
            os.makedirs(self.userfolder)
        if not os.path.exists(self.moderatorfolder):
            os.makedirs(self.moderatorfolder)
        if not os.path.exists(self.modelfolder):
            os.makedirs(self.modelfolder)

    def run(self):
        print("Run Routes")
        self.check_folders()
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

        @app.get("/upload", response_class=HTMLResponse)
        async def upload(request: Request):
            context = {"request": request}
            return templates.TemplateResponse("upload.html", context)


        # @app.get("/type", response_class=HTMLResponse)
        # async def type(request: Request):
        #     types = os.listdir('static/clothes/')
        #     number_of_types = len(types)
        #     print(types)
        #     context = {"request": request}
        #     context["types"] = types
        #     context["number_of_types"] = number_of_types
        #     return templates.TemplateResponse("type.html", context)

        @app.get("/camera", response_class=HTMLResponse)
        async def camera_get(request: Request):
            context = {"request": request}
            return templates.TemplateResponse("camera.html", context)

        @app.post("/uploaded",response_class=HTMLResponse)
        async def uploaded(image: UploadFile = File(...)):
            try:
                contents = await image.read()
                with open("uploaded_" + image.filename, "wb") as f:
                    f.write(contents)
            except Exception:
                return "There was an error uploading the file"
            finally:
                await image.close()
            pred = pred_model(["./uploaded_image.jpeg"], "./Utils/Imageclassifier.pt")
            
            return f"prediction: {pred}"

        # @app.post("/submitform",response_class=HTMLResponse)
        @app.post("/submitform")
        async def handle_form(request:Request, my_picture_file:UploadFile = File(...)):
            image_name = str(uuid.uuid4())
            extension = my_picture_file.filename.split(".")[-1]
            picture_name = image_name + "." + extension
            #picture_name = "uploaded_" + my_picture_file.filename
            try:
                print("entering the try")
                contents = await my_picture_file.read()
                with open(f"./data/{picture_name}", "wb") as f:
                    f.write(contents)
            except Exception:
                print("entering the except")
                return "There was an error uploading the file"
            finally:
                await my_picture_file.close()
            pred = pred_model([f"./data/{picture_name}"], "./Utils/Imageclassifier.pt")
            context = {"request":request}
            context["filename"] = my_picture_file.filename
            context["predictions"] = pred#to take only the string
            context["predictions_percentage"] = pred.items() #to take only the string
            context["picture_name"] = picture_name
            print(pred)
            return templates.TemplateResponse("detected.html",context)


        #      @app.post("/upload")
        # async def upload(image: UploadFile = File(...)):
        #     try:
        #         contents = await image.read()
        #         "create uud id for image name and add original extension"
        #         extension = image.filename.split(".")[-1]
        #         image_name = str(uuid.uuid4())
        #         image_name_ext = image_name + "." + extension
        #         with open(self.uploadfolder + image_name_ext, "wb") as f:
        #             f.write(contents)
        #     except Exception:
        #         return "There was an error uploading the file"
        #     finally:
        #         await image.close()
        #     pred = pred_model([self.uploadfolder + image_name_ext], "./Utils/Imageclassifier.pt")
        #     with open(self.uploadfolder + image_name + ".txt", "w") as f:
        #         f.write(str(pred))
        #     return f"Prediction: {pred} of {image_name_ext}"

        