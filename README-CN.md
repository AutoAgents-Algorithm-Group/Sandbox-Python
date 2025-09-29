<div align="center">

<img src="https://img.shields.io/badge/-Sandbox--Python-000000?style=for-the-badge&labelColor=faf9f6&color=faf9f6&logoColor=000000" alt="Sandbox-Python" width="280"/>

<h4>安全的Python代码执行环境</h4>

[English](README.md) | 简体中文

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="media/dark_license.svg" />
  <img alt="License MIT" src="media/light_license.svg" />
</picture>

</div>

专为大语言模型设计的安全Python代码执行沙盒API，为AI驱动的代码执行和验证提供安全隔离的环境。

## 目录
- [目录](#目录)
- [为什么选择Sandbox-Python？](#为什么选择sandbox-python)
- [快速开始](#快速开始)
- [API文档](#api文档)
  - [核心接口](#核心接口)
    - [健康检查](#健康检查)
    - [代码执行](#代码执行)
  - [使用示例](#使用示例)
    - [Python客户端](#python客户端)
    - [cURL](#curl)
- [部署](#部署)
  - [项目结构](#项目结构)
  - [使用场景](#使用场景)
  - [配置说明](#配置说明)
    - [环境变量](#环境变量)
    - [端口配置](#端口配置)
- [安全建议](#安全建议)
- [贡献](#贡献)
- [许可证](#许可证)

## 为什么选择Sandbox-Python？

Sandbox-Python是一个革命性的代码执行服务，让AI系统能够以前所未有的安全性和可靠性安全执行Python代码。如同保护您基础设施的堡垒，Sandbox-Python为您的AI应用程序提供了蓬勃发展的基础和安全环境。

- **安全至上**：隔离的执行环境，保护您的系统免受恶意代码侵害
- **AI优化**：专门为大语言模型集成和代码验证而设计
- **高性能**：基于FastAPI构建，提供闪电般的响应速度
- **生产就绪**：基于Docker的部署，具备健康监控和自动恢复功能
- **开发者友好**：全面的API文档和简单的集成方式

## 快速开始

**先决条件**
- Python 3.11+
- Docker

**开始使用**
```bash
# 1. 克隆仓库
git clone https://github.com/Hehua-Fan/Sandbox-Python.git
cd Sandbox-Python

# 2. 使用Docker Compose启动
docker compose -f docker/docker-compose.yml up -d
```

**本地开发**
```bash
# 1. 安装依赖
pip install -r backend/requirements.txt

# 2. 启动开发服务器
cd backend/api
uvicorn main:app --host 0.0.0.0 --port 8005 --reload
```

## API文档

在以下地址访问交互式API文档：http://localhost:8005/docs

### 核心接口

#### 健康检查
```http
GET /health
```

**响应：**
```json
{
  "message": "Frank Sandbox API is running"
}
```

#### 代码执行
```http
POST /sandbox_run_code
```

**请求体：**
```json
{
  "code": "print('Hello, World!')\nresult = 1 + 1\nprint(f'1 + 1 = {result}')"
}
```

**响应：**
```json
{
  "result": "Hello, World!\n1 + 1 = 2\n"
}
```

### 使用示例

#### Python客户端
```python
import requests

# 远程执行Python代码
url = "http://localhost:8005/sandbox_run_code"
code = """
import pandas as pd
import numpy as np

# 创建示例数据
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# 计算统计信息
print(f"\\nA列的和: {df['A'].sum()}")
print(f"B列的均值: {df['B'].mean()}")
"""

response = requests.post(url, json={"code": code})
result = response.json()
print("执行结果:")
print(result["result"])
```

#### cURL
```bash
curl -X POST "http://localhost:8005/sandbox_run_code" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "for i in range(5):\n    print(f\"数字: {i}\")"
  }'
```

## 部署

**Docker**
```bash
cd Sandbox-Python
docker compose -f docker/docker-compose.yml up -d
```

**生产环境**
```yaml
# docker-compose.prod.yml
services:
  sandbox-python:
    build:
      context: .
      dockerfile: docker/Dockerfile
    ports:
      - "8005:8005"
    environment:
      - PYTHONPATH=/app
      - PYTHON_ENV=production
    restart: always
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
```

**故障排除**
```bash
# 查看应用日志
docker compose -f docker/docker-compose.yml logs -f app

# 停止并删除容器
docker stop sandbox-python && docker rm sandbox-python
docker rmi sandbox-python-app

# 重启服务
docker compose -f docker/docker-compose.yml restart
```

### 项目结构

```
Sandbox-Python/
├── backend/
│   ├── api/
│   │   └── main.py          # FastAPI应用程序
│   └── requirements.txt     # Python依赖
├── docker/
│   ├── Dockerfile          # 容器构建配置
│   ├── docker-compose.yml  # 服务编排
│   └── start.sh            # 应用启动脚本
├── media/                  # 静态资源
├── .gitignore             # Git忽略规则
└── README.md              # 项目文档
```

### 使用场景

- **AI代码生成**：安全验证LLM生成的Python代码
- **数据分析助手**：为AI系统提供数据处理能力
- **算法原型设计**：快速测试算法逻辑和性能
- **教育工具**：在线Python代码教学和演示
- **自动化测试**：代码质量检查和单元测试执行

### 配置说明

#### 环境变量

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `PYTHONPATH` | `/app` | Python模块搜索路径 |
| `PYTHON_ENV` | `production` | Python运行环境 |

#### 端口配置

- **默认端口**：8005
- **健康检查**：`/health`
- **API文档**：`/docs`
- **ReDoc文档**：`/redoc`

## 安全建议

- 在生产环境中使用反向代理（如Nginx）
- 配置适当的资源限制
- 定期更新依赖包
- 监控沙盒执行时间和资源使用

## 贡献

1. Fork 此仓库
2. 创建您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 许可证

本项目采用MIT许可证 - 详情请查看 [LICENSE](LICENSE) 文件。
