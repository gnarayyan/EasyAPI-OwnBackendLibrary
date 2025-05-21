from easyapi.main import EasyAPI
from easyapi.utils.request import Request
from easyapi.utils.response import Response


app = EasyAPI()

@app.get('/users')
async def get_users(req:Request, res:Response):
  await res.json(['rivaan', 'naman'])

@app.get('/user')
async def get_users(req:Request, res:Response):
  
  await res.send( status=400, message={"message": "Success","name" :'rivaan'}, content_type='application/json')

@app.get("/hello")
async def hello_handler(req:Request, res:Response):
    
    # name = params.get("name", ["world"])[0]
    await res.text(f"Hello, Narayan!") 