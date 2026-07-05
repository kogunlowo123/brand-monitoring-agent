"""Test configuration for Brand Monitoring Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "brand-monitoring-agent", "category": "Marketing"}
