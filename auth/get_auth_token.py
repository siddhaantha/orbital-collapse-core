def get_auth_token():
    return "SECURE TOKEN"

# 🔥 make module callable like function
import sys
sys.modules[__name__] = get_auth_token
