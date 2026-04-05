from auth.login import authenticate
from telemetry.parser import parse_signal
from launch-sequence.dispatcher import dispatch_command
from ground-control.dashboard import display_status

def run_system():
    print("\n==============================")
    print("🛰️  ORBITAL COLLAPSE SYSTEM")
    print("==============================\n")

    print(authenticate())
    print(parse_signal())
    print(dispatch_command())
    print(display_status())

    print("\n==============================")
    print("✅ SYSTEM STABLE")
    print("==============================\n")

if __name__ == "__main__":
    run_system()
