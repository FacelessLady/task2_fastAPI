from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"FIO": "Шмит Ангелина Алексеевна"}

@app.get('/users')
async def f_indexT():
     return {"Contact details": "users", "phone": "89831023404"}

@app.get('/tools')
async def f_indexT():
     return {"Data": "tools", "Developer Skills": "Знание нескольких языков программирования, компьютерные сети"}