from fastapi import FastAPI
import uvicorn

## web application
app = FastAPI()

# GET / HTTP/1.1
# HOST: 0.0.0.0
# PATH: /
# Content-Type: application/json
# Content-Length: 23
# {"message": "Hello World"}

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    ## protocol server
    uvicorn.run(app, host="0.0.0.0", port=8001)
