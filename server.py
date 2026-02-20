import http.server
import socketserver
import webbrowser
import os
import socket
from contextlib import closing

def find_free_port():
    """Find a free port to use"""
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

PORT = find_free_port()
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # Allow reuse of address
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("="*60)
            print("🚀 Financial Forensics Engine - Money Muling Detector")
            print("="*60)
            print(f"📁 Serving directory: {DIRECTORY}")
            print(f"🌐 Server running at: http://localhost:{PORT}")
            print("\n📊 Open these pages:")
            print(f"   Dashboard: http://localhost:{PORT}/dashboard.html")
            print(f"   Analysis:  http://localhost:{PORT}/analysis.html")
            print(f"   Reports:   http://localhost:{PORT}/reports.html")
            print(f"   Settings:  http://localhost:{PORT}/settings.html")
            print("\n📁 Data file: data/money-muling.csv")
            print(f"   Total transactions: 279")
            print("\n🔄 Detected fraud patterns:")
            print("   • Cycle 1: ACC_00123 → ACC_00456 → ACC_00789")
            print("   • Cycle 2: ACC_00234 → ACC_00567 → ACC_00890")
            print("   • Cycle 3: ACC_00345 → ACC_00678 → ACC_00901")
            print("   • Smurfing: SMURF_01 (12 transactions)")
            print("   • Smurfing: MERCHANT_01 (20 transactions)")
            print("\n⚠️  Press Ctrl+C to stop the server")
            print("="*60)
            
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}/dashboard.html')
            
            # Start server
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use.")
            print("🔄 Trying another port...")
            # Try another port
            new_port = PORT + 1
            with socketserver.TCPServer(("", new_port), Handler) as httpd:
                print(f"✅ Server started on port {new_port}")
                print(f"🌐 http://localhost:{new_port}/dashboard.html")
                webbrowser.open(f'http://localhost:{new_port}/dashboard.html')
                httpd.serve_forever()
        else:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
