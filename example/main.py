from easyapi.main import EasyAPI


app = EasyAPI()

@app.get('/users')
def get_users(req, res):
  res.send(['rivaan', 'naman'])

@app.get('/user')
def get_users(req, res):
  res.send('rivaan')