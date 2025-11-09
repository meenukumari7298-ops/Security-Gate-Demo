import pickle
import jwt
import random
import subprocess
from flask import Flask, request
import yaml
import os

app = Flask(__name__)

# 1. Hardcoded AWS key
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
# 2. Hardcoded JWT secret
JWT_SECRET = "my-super-secret-jwt-key"
# 3. Hardcoded Stripe key
STRIPE_KEY = "sk_live_51J1234567890abcdefABCDEF"
# 4. Hardcoded Okta key
OKTA_KEY = "00abc123def456ghi789jkl012mno345pqr678stu"

# 5. Pickle RCE
data = pickle.loads(request.data)

# 6. Weak random
token = random.random()

# 7. Debug mode in Flask
app.run(debug=True)

# 8. Command injection
subprocess.run(f"echo {request.args.get('name')}", shell=True)

# 9. Insecure YAML deserialization
config = yaml.load(request.files['file'].stream, Loader=yaml.Loader)

# 10. Hardcoded password
if request.form['pass'] == "admin123":
    print("Login success")
# This PR is intentionally vulnerable for security gate demo
