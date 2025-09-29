#!/bin/bash

# 激活虚拟环境
source /opt/venv/bin/activate

# 设置环境变量
export PYTHONPATH=/app
export VIRTUAL_ENV=/opt/venv

# 启动FastAPI应用
exec uvicorn main:app --host 0.0.0.0 --port 8005
