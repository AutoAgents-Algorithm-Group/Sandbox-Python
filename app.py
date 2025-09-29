from fastapi import FastAPI
from pydantic import BaseModel
from autoagents_core.sandbox import LocalSandboxService
from autoagents_core.utils.extractor import extract_python_code

app = FastAPI(title="Frank Sandbox API", description="Frank Sandbox API", version="1.0.0")

class SandboxRequest(BaseModel):
    code: str = "print('This is frank sandbox service')"

class SandboxResponse(BaseModel):
    result: str

@app.get("/")
async def root():
    return {"message": "Frank Sandbox API is running"}

@app.get("/health")
async def root():
    return {"message": "Frank Sandbox API is running"}

@app.post("/sandbox_run_code", response_model=SandboxResponse)
async def sandbox_run_code(request: SandboxRequest):
    """
    创建沙盒并运行代码
    """
    sandbox = LocalSandboxService()
    code = extract_python_code(request.code)
    result = sandbox.run_code(code=code)
    return SandboxResponse(result=str(result))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
    # uvicorn app:app --host 0.0.0.0 --port 8005 --reload