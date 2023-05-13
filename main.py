#type: ignore
from method.dummy import Echoinput
from fastapi import FastAPI, File, UploadFile, Request, Form
import shutil 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 

app = FastAPI()
templates = Jinja2Templates(directory="templates") 
model = "/models"


@app.get("/")
async def read_root(request: Request):
   return templates.TemplateResponse("main.html", {"request": request})

@app.get("/upload/", response_class=HTMLResponse)
async def upload(request: Request):
   return templates.TemplateResponse("uploadfile.html", {"request": request})


@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File(...), filename: str = Form(...)):
   if (file.content_type != "text/csv"):
    return Echoinput("notCSVfromMethod")
   else:
    with open("uploaddata/"+filename +".csv", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        return {"filename": file.filename}

@app.get("/predict/", response_class=HTMLResponse)
async def upload(request: Request):
   return templates.TemplateResponse("irisform.html", {"request": request})

@app.post("/predictor/")
async def predictor(sepallength: int= Form(...), sepalwidth: int= Form(...), petallength: int= Form(...), petalwidth: int= Form(...)):
   return sepallength, sepalwidth, petallength, petalwidth