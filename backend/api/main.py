from fastapi import FastAPI
from pydantic import BaseModel
from autoagents_core.sandbox import LocalSandboxService
from autoagents_core.utils.extractor import extract_python_code
from typing import Optional
import re
import json

app = FastAPI(title="Frank Sandbox API", description="Frank Sandbox API", version="1.0.0")

class SandboxRequest(BaseModel):
    sdk_code: str
    jwt_token: str

class SandboxResponse(BaseModel):
    result: str
    workflow_id: Optional[str] = None



def extract_workflow_id(stdout: str) -> Optional[str]:
    """
    从标准输出中提取 workflow_id
    支持多种格式：
    1. WORKFLOW_ID:xxxxx
    2. {"workflow_id": "xxxxx"}
    3. 最后一行的纯文本（作为兜底）
    """
    if not stdout:
        return None
    
    # 方法1：查找 WORKFLOW_ID: 标记
    match = re.search(r'WORKFLOW_ID:(\S+)', stdout)
    if match:
        return match.group(1).strip()
    
    # 方法2：查找 JSON 格式
    try:
        # 尝试查找 JSON 块
        json_match = re.search(r'\{[^{}]*"workflow_id"[^{}]*\}', stdout)
        if json_match:
            data = json.loads(json_match.group(0))
            return data.get('workflow_id')
    except:
        pass
    
    # 方法3：获取最后一行非空内容（兜底方案）
    lines = [line.strip() for line in stdout.strip().split('\n') if line.strip()]
    if lines:
        last_line = lines[-1]
        # 如果最后一行看起来像 ID（数字、字母、下划线、连字符的组合）
        if re.match(r'^[a-zA-Z0-9_-]+$', last_line):
            return last_line
    
    return None

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
    workflow_id = extract_workflow_id(result.get('stdout', ''))
    return SandboxResponse(result=str(result), workflow_id=workflow_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
    # uvicorn app:app --host 0.0.0.0 --port 8005 --reload