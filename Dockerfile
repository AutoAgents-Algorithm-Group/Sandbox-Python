# 使用官方Python运行时作为父镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 创建虚拟环境
RUN python -m venv /opt/venv

# 激活虚拟环境并升级pip
RUN /opt/venv/bin/pip install --upgrade pip

# 将虚拟环境的bin目录添加到PATH
ENV PATH="/opt/venv/bin:$PATH"

# 复制requirements.txt文件
COPY requirements.txt .

# 在虚拟环境中安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app.py .

# 暴露端口
EXPOSE 8005

# 设置环境变量
ENV PYTHONPATH=/app
ENV VIRTUAL_ENV=/opt/venv

# 运行应用（使用虚拟环境中的uvicorn）
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8005"]