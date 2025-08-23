# 使用官方Python运行时作为父镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制requirements.txt文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app.py .

# 暴露端口
EXPOSE 8005

# 设置环境变量
ENV PYTHONPATH=/app

# 运行应用
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8005"]