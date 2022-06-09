import uvicorn
from Utils.routes import Routes

routes = Routes()


app = routes.run()
uvicorn.run(app)
