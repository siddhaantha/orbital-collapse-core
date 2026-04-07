from auth import login
from telemetry import parser
from ground_control import dashboard
from launch_sequence import dispatcher


EXPECTED = [
    "[AUTH] Operator verified",
    "[TELEMETRY] Data stream nominal",
    "[DISPATCH] Command sent successfully",
    "[GROUND] Dashboard v2 — satellite grid online"
]


def check_auth():
    return login.authenticate()


def check_telemetry():
    return parser.parse_signal()


def check_dispatch():
    return dispatcher.dispatch()


def check_ground():
    try:
        return dashboard.display_status()
    except Exception:
        return "[GROUND] ERROR"


def run_all_checks():
    results = [
        check_auth(),
        check_telemetry(),
        check_dispatch(),
        check_ground()
    ]

    for r in results:
        print(r)

    if results == EXPECTED:
        print("✅ SYSTEM STABLE")
    else:
        print("❌ SYSTEM NOT STABLE")


if __name__ == "__main__":
    run_all_checks()