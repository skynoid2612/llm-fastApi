from fastapi import FastAPI, HTTPException
from llm_model import generate_response

app = FastAPI()


@app.get("/generate-response/")
async def get_response(prompt: str):
    if not prompt:
        raise HTTPException(status_code=400, detail="Please provide a prompt.")
    response = generate_response(prompt)
    if response["status"]:
        return response
    else:
        raise HTTPException(status_code=500, detail="Internal server error")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
