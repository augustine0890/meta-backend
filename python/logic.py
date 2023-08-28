import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env == LOCAL:
    print("Local environment")
else:
    print("Unknown environment")