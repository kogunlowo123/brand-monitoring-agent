# Brand Monitoring Agent

[![CI](https://github.com/kogunlowo123/brand-monitoring-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/brand-monitoring-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Marketing | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Brand monitoring agent that tracks brand mentions, analyzes sentiment trends, detects reputation risks, monitors competitor activity, and generates brand health reports.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `track_mentions` | Track brand mentions across web, social, and news sources |
| `analyze_sentiment_trend` | Analyze sentiment trends over time for brand mentions |
| `detect_reputation_risk` | Detect emerging reputation risks from mention analysis |
| `monitor_competitors` | Monitor competitor brand mentions and sentiment |
| `generate_brand_report` | Generate brand health report with SOV and sentiment metrics |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/brand-monitoring/create` | Create or generate |
| `POST` | `/api/v1/brand-monitoring/analyze` | Analyze performance |
| `POST` | `/api/v1/brand-monitoring/optimize` | Optimize |
| `POST` | `/api/v1/brand-monitoring/schedule` | Schedule |
| `POST` | `/api/v1/brand-monitoring/report` | Generate report |

## Features

- Brand
- Monitoring
- Analytics
- Optimization

## Integrations

- Hubspot Marketing
- Marketo
- Mailchimp
- Google Analytics
- Meta Ads

## Architecture

```
brand-monitoring-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── brand_monitoring_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Marketing Platform + LLM + Analytics**

---

Built as part of the Enterprise AI Agent Platform.
