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
COPY backend/requirements.txt .

# 在虚拟环境中安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY backend/api/main.py .

# 复制启动脚本
COPY docker/start.sh .

# 设置启动脚本权限
RUN chmod +x start.sh

# 暴露端口
EXPOSE 8005

# 设置环境变量
ENV PYTHONPATH=/app
ENV VIRTUAL_ENV=/opt/venv

# 运行应用（使用启动脚本）
CMD ["./start.sh"]