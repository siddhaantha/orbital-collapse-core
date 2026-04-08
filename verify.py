
"""
Version Control Wars - System Verify Script
"""

import sys
from launch_sequence import dispatcher


try:
    from ground_control.status import system_health
except ImportError:
    dashboard = None

def check_system():
    print("=== SYSTEM INTEGRITY CHECK ===")
    
    status_ok = True
    
   
    try:
        launch_sequence()
        print("✅ Launch sequence: OK")
    except Exception as e:
        print("❌ Launch sequence failed")
        status_ok = False

    try:
        from telemetry import parse_signal
        result = parse_signal("SIGNAL:42")
        if "42" in result and "STABLE" in result:
            print("✅ Telemetry: OK")
        else:
            print("❌ Telemetry mismatch")
            status_ok = False
    except Exception:
        print("❌ Telemetry module issue")
        status_ok = False
    
    
    try:
        from auth import get_auth_token
        token = get_auth_token()
        if "SECURE" in token:
            print("✅ Authentication: OK")
        else:
            print("❌ Authentication failed")
            status_ok = False
    except Exception:
        print("❌ Auth module issue")
        status_ok = False
    
    
    if dashboard is None:
        print("❌ Dashboard module missing")
        status_ok = False
    else:
        try:
            status = dashboard.get_status() if hasattr(dashboard, 'get_status') else dashboard()
            expected = "[GROUND] Dashboard v2 — satellite grid online"
            if status == expected:
                print("✅ Dashboard: OK")
            else:
                print("❌ Dashboard wrong output")
                status_ok = False
        except Exception:
            print("❌ Dashboard execution error")
            status_ok = False
    
    if status_ok:
        print("\n✅ SYSTEM STABLE")
        print("All missions completed successfully!")
        return True
    else:
        print("\n❌ SYSTEM NOT STABLE")
        print("Complete all 8 missions to stabilize the system.")
        return False

if __name__ == "__main__":
    check_system()
