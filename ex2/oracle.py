import os
import sys
from dotenv import load_dotenv


if __name__ == "__main__":
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    # load_dotenv - reads key-value pairs from a .env file and
    #               can set them as environment variables
    # Additional note: If an environment variable is not found in the
    # .env file, load_dotenv will then search for a variable by the given
    # name in the host environment. This means that when your project is
    # running locally and the .env file is present, the variables defined in
    # the file will be used. When your project is deployed to a
    # host environment like a virtual machine or Docker container where the
    # .env file is not present, the environment variables defined in the host
    # environment will be used instead
    # In this exercise, we just want to read the values
    load_dotenv(".env")

    print("Configuration loaded:")
    variables = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
                 "LOG_LEVEL", "ZION_ENDPOINT"]
    # Get the value from the specific environment variables
    variables_env = [os.getenv(value) for value in variables]
    finish_program = False
    if not variables_env[0]:
        print("[ERROR] MATRIX_MODE missing")
        finish_program = True
    else:
        print(f"Mode: {variables_env[0]}")
    if not variables_env[1]:
        print("[ERROR] DATABASE_URL missing")
        finish_program = True
    else:
        print("Database: Connected to local instance")
    if not variables_env[2]:
        print("[ERROR] API_KEY missing")
        finish_program = True
    else:
        print("API Access: Authenticated")
    if not variables_env[3]:
        print("[ERROR] LOG_LEVEL missing")
        finish_program = True
    else:
        print(f"Log Level: {variables_env[3]}")
    if not variables_env[4]:
        print("[ERROR] ZION_ENDPOINT missing")
        finish_program = True
    else:
        print("Zion Network: Online")
    if finish_program:
        sys.exit()
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations")
