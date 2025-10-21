from fastapi import FastAPI
from pydantic import BaseModel
from autoagents_core.sandbox import LocalSandboxService
from autoagents_core.utils.extractor import extract_python_code

app = FastAPI(title="Frank Sandbox API", description="Frank Sandbox API", version="1.0.0")

class SandboxRequest(BaseModel):
    sdk_code: str
    jwt_token: str

class SandboxResponse(BaseModel):
    result: str

@app.get("/")
async def root():
    return {"message": "Frank Sandbox API is running"}

@app.get("/health")
async def root():
    return {"message": "Frank Sandbox API is running"}

@app.post("/run_code", response_model=SandboxResponse)
async def sandbox_run_code(request: SandboxRequest):
    """
    创建沙盒并运行代码
    """
    sandbox = LocalSandboxService()
    sdk_code = extract_python_code(request.sdk_code).replace("jwt_token=\"\"", f"jwt_token=\"{request.jwt_token}\"")
    result = sandbox.run_code(code=sdk_code)
    return SandboxResponse(result=str(result))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
    # uvicorn app:app --host 0.0.0.0 --port 8005 --reload