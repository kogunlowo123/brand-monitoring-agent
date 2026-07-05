"""Brand Monitoring Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_track_mentions():
    """Test Track brand mentions across web, social, and news sources."""
    tools = AgentTools()
    result = await tools.track_mentions(brand_name="test", sources="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_sentiment_trend():
    """Test Analyze sentiment trends over time for brand mentions."""
    tools = AgentTools()
    result = await tools.analyze_sentiment_trend(brand_name="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_reputation_risk():
    """Test Detect emerging reputation risks from mention analysis."""
    tools = AgentTools()
    result = await tools.detect_reputation_risk(brand_name="test", risk_categories="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_monitor_competitors():
    """Test Monitor competitor brand mentions and sentiment."""
    tools = AgentTools()
    result = await tools.monitor_competitors(competitors="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.brand_monitoring_agent_agent import BrandMonitoringAgentAgent
    agent = BrandMonitoringAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
