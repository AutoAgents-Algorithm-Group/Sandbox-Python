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
- [部署](#部署)
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

## 部署

**Docker**
```bash
cd Sandbox-Python
docker compose -f docker/docker-compose.yml up -d
```

**故障排除**
```bash
# 查看应用日志
docker compose -f docker/docker-compose.yml logs -f app

# 停止并删除容器
docker stop sandbox-python && docker rm sandbox-python
docker rmi sandbox-python-app
```

## 贡献

1. Fork 此仓库
2. 创建您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 许可证

本项目采用MIT许可证 - 详情请查看 [LICENSE](LICENSE) 文件。
