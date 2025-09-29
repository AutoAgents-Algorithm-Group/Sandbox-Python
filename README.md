<div align="center">

<img src="https://img.shields.io/badge/-Sandbox--Python-000000?style=for-the-badge&labelColor=faf9f6&color=faf9f6&logoColor=000000" alt="Sandbox-Python" width="280"/>

<h4>Secure Python Code Execution Environment</h4>

English | [简体中文](README-CN.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="media/dark_license.svg" />
  <img alt="License MIT" src="media/light_license.svg" />
</picture>

</div>

A secure Python code execution sandbox API designed specifically for Large Language Models, providing a safe and isolated environment for AI-driven code execution and validation.

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Why Sandbox-Python?](#why-sandbox-python)
- [Quick Start](#quick-start)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Why Sandbox-Python?

Sandbox-Python is a revolutionary code execution service that empowers AI systems to safely execute Python code with unprecedented security and reliability. Like a fortress protecting your infrastructure, Sandbox-Python provides the foundation and secure environment for your AI applications to flourish.

- **Security First**: Isolated execution environment that protects your system from malicious code
- **AI-Optimized**: Specifically designed for Large Language Model integration and code validation
- **High Performance**: Built on FastAPI for lightning-fast response times
- **Production Ready**: Docker-based deployment with health monitoring and auto-recovery
- **Developer Friendly**: Comprehensive API documentation and easy integration

## Quick Start

**Prerequisites**
- Python 3.11+
- Docker

**Get Started**
```bash
# 1. Clone the repository
git clone https://github.com/Hehua-Fan/Sandbox-Python.git
cd Sandbox-Python

# 2. Start with Docker Compose
docker compose -f docker/docker-compose.yml up -d
```

## Deployment

**Docker**
```bash
cd Sandbox-Python
docker compose -f docker/docker-compose.yml up -d
```

**Troubleshooting**
```bash
# View application logs
docker compose -f docker/docker-compose.yml logs -f app

# Stop and remove containers
docker stop sandbox-python && docker rm sandbox-python
docker rmi sandbox-python-app
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.