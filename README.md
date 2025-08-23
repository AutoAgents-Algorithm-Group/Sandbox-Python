# Frank Sandbox API

🚀 一个为大语言模型提供安全Python代码执行环境的FastAPI服务

## 📋 项目简介

Frank Sandbox API 是一个专门为大语言模型设计的Python代码执行沙盒服务。它提供了一个安全、隔离的环境，让AI模型可以安全地执行Python代码并获取结果，支持代码生成、数据分析、算法验证等多种AI应用场景。

## ✨ 功能特点

- 🔒 **安全沙盒环境**：隔离的Python代码执行环境，保障系统安全
- ⚡ **高性能API**：基于FastAPI构建，提供快速响应的RESTful接口
- 🐳 **Docker支持**：完整的容器化部署方案，开箱即用
- 🩺 **健康检查**：内置健康监控端点，便于运维管理
- 📝 **智能代码提取**：自动提取和清理Python代码片段
- 🔌 **易于集成**：标准化的API接口，方便与各类AI系统集成

## 🛠 技术栈

- **Web框架**：FastAPI
- **运行环境**：Python 3.11+
- **沙盒引擎**：autoagentsai
- **容器化**：Docker + Docker Compose
- **依赖管理**：pip + requirements.txt

## 🚀 快速开始

### 方式一：Docker Compose（推荐）

```bash
# 克隆项目
git clone https://github.com/Hehua-Fan/Sandbox-Python.git
cd Sandbox-Python

# 使用Docker Compose启动服务
docker-compose up -d

# 检查服务状态
curl http://localhost:8005/health
```

### 方式二：Docker 直接运行

```bash
# 构建镜像
docker build -t frank-sandbox-api .

# 运行容器
docker run -d \
  --name frank-sandbox \
  -p 8005:8005 \
  frank-sandbox-api
```

### 方式三：本地开发环境

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
python app.py

# 或使用uvicorn
uvicorn app:app --host 0.0.0.0 --port 8005 --reload
```

## 📡 API 文档

服务启动后访问：http://localhost:8005/docs 查看完整的Swagger API文档

### 核心接口

#### 1. 健康检查

```http
GET /health
```

响应：
```json
{
  "message": "Frank Sandbox API is running"
}
```

#### 2. 代码执行

```http
POST /sandbox_run_code
```

请求体：
```json
{
  "code": "print('Hello, World!')\nresult = 1 + 1\nprint(f'1 + 1 = {result}')"
}
```

响应：
```json
{
  "result": "Hello, World!\n1 + 1 = 2\n"
}
```

### 使用示例

#### Python 客户端示例

```python
import requests

# API端点
url = "http://localhost:8005/sandbox_run_code"

# 要执行的Python代码
code = """
import pandas as pd
import numpy as np

# 创建示例数据
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# 计算统计信息
print(f"\\nSum of column A: {df['A'].sum()}")
print(f"Mean of column B: {df['B'].mean()}")
"""

# 发送请求
response = requests.post(url, json={"code": code})
result = response.json()

print("执行结果:")
print(result["result"])
```

#### cURL 示例

```bash
curl -X POST "http://localhost:8005/sandbox_run_code" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "for i in range(5):\n    print(f\"Number: {i}\")"
  }'
```

## 🔧 配置说明

### 环境变量

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `PYTHONPATH` | `/app` | Python模块搜索路径 |

### 端口配置

- **默认端口**：8005
- **健康检查**：`/health`
- **API文档**：`/docs`
- **ReDoc文档**：`/redoc`

## 🏗 部署建议

### 生产环境

```yaml
# docker-compose.prod.yml
services:
  frank-sandbox-api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8005:8005"
    environment:
      - PYTHONPATH=/app
    restart: always
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8005/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### 安全建议

- 在生产环境中使用反向代理（如Nginx）
- 配置适当的资源限制
- 定期更新依赖包
- 监控沙盒执行时间和资源使用

## 🤝 使用场景

- **AI代码生成验证**：验证大语言模型生成的Python代码
- **数据分析助手**：为AI提供数据处理和分析能力
- **算法原型测试**：快速验证算法逻辑和性能
- **教育辅助工具**：在线Python代码教学和演示
- **自动化测试**：代码质量检查和单元测试执行

## 📝 开发说明

### 项目结构

```
Sandbox-Python/
├── app.py              # FastAPI应用主文件
├── requirements.txt    # Python依赖包
├── Dockerfile         # Docker构建文件
├── docker-compose.yml # Docker编排配置
├── .gitignore        # Git忽略规则
└── README.md         # 项目说明文档
```

### 本地开发

```bash
# 安装开发依赖
pip install -r requirements.txt

# 启动开发服务器（支持热重载）
uvicorn app:app --host 0.0.0.0 --port 8005 --reload
```

## 🐛 故障排除

### 常见问题

1. **端口占用**：确保8005端口未被其他服务占用
2. **依赖安装失败**：检查Python版本是否为3.11+
3. **Docker构建失败**：确保Docker服务正常运行

### 日志查看

```bash
# Docker Compose日志
docker-compose logs -f

# 容器日志
docker logs frank-sandbox-api
```

## 📄 许可证

MIT License - 详情请查看 [LICENSE](LICENSE) 文件

## 🙋‍♂️ 贡献指南

欢迎提交Issue和Pull Request！在提交之前请确保：

1. 代码符合PEP 8规范
2. 添加必要的测试用例
3. 更新相关文档

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- GitHub Issues: [提交Issue](https://github.com/Hehua-Fan/Sandbox-Python/issues)
- Email: 你的邮箱地址

---

⭐ 如果这个项目对你有帮助，请给个Star支持一下！
