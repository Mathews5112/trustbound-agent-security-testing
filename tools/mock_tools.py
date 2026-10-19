
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "synthetic_data"

# All changes exist only in this Python process.
ACTIONS = []


def load_data(filename):
    path = DATA_DIR / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_logs(query=""):
    logs = load_data("logs.json")

    return [
        log for log in logs
        if query.lower() in json.dumps(log).lower()
    ]


def open_ticket(ticket_id=""):
    tickets = load_data("tickets.json")

    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            return ticket

    return {"error": "Ticket not found"}


def retrieve_runbook(runbook_id=""):
    runbooks = load_data("runbooks.json")

    for runbook in runbooks:
        if runbook["id"] == runbook_id:
            return runbook

    return {"error": "Runbook not found"}


def save_report(report=""):
    action = {
        "tool": "save_report",
        "report": report,
        "status": "simulated"
    }
    ACTIONS.append(action)
    return action


def send_notification(message=""):
    action = {
        "tool": "send_notification",
        "message": message,
        "status": "simulated"
    }
    ACTIONS.append(action)
    return action


def block_ip(ip_address=""):
    action = {
        "tool": "block_ip",
        "ip_address": ip_address,
        "status": "simulated"
    }
    ACTIONS.append(action)
    return action


def isolate_host(hostname=""):
    action = {
        "tool": "isolate_host",
        "hostname": hostname,
        "status": "simulated"
    }
    ACTIONS.append(action)
    return action


TOOLS = {
    "search_logs": search_logs,
    "open_ticket": open_ticket,
    "retrieve_runbook": retrieve_runbook,
    "save_report": save_report,
    "send_notification": send_notification,
    "block_ip": block_ip,
    "isolate_host": isolate_host
}


def execute_tool(name, arguments):
    if name not in TOOLS:
        return {"error": f"Unknown tool: {name}"}

    if not isinstance(arguments, dict):
        return {"error": "Arguments must be a JSON object"}

    try:
        return TOOLS[name](**arguments)
    except TypeError as error:
        return {"error": str(error)}
