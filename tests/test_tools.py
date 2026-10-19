
from tools.mock_tools import (
    ACTIONS,
    search_logs,
    open_ticket,
    retrieve_runbook,
    save_report,
    send_notification,
    block_ip,
    isolate_host,
    execute_tool
)


def test_search_logs():
    results = search_logs("SSH")
    assert len(results) >= 2


def test_open_ticket():
    result = open_ticket("INC-001")
    assert result["ticket_id"] == "INC-001"


def test_retrieve_runbook():
    result = retrieve_runbook("RB-001")
    assert result["id"] == "RB-001"


def test_save_report():
    ACTIONS.clear()
    result = save_report("Test report")
    assert result["status"] == "simulated"
    assert len(ACTIONS) == 1


def test_send_notification():
    result = send_notification("Test alert")
    assert result["status"] == "simulated"


def test_block_ip():
    result = block_ip("192.0.2.10")
    assert result["status"] == "simulated"


def test_isolate_host():
    result = isolate_host("LAB-PC-01")
    assert result["status"] == "simulated"


def test_tool_dispatch():
    result = execute_tool(
        "open_ticket",
        {"ticket_id": "INC-001"}
    )
    assert result["ticket_id"] == "INC-001"


def test_unknown_tool():
    result = execute_tool("unknown_tool", {})
    assert "error" in result
