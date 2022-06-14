import uvicorn
from Utils.routes import Routes

routes = Routes()


app = routes.run()
uvicorn.run(app)

#if __name__ == "__main__":
#    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)