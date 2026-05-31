import http.server
import socketserver
import os

PORT = 3000

# Cambiar al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), handler)

print(f"╔════════════════════════════════════════════╗")
print(f"║  Servidor web funcionando en puerto {PORT}   ║")
print(f"║  URL: http://localhost:{PORT}              ║")
print(f"║  Red local: http://<tu-ip>:{PORT}          ║")
print(f"║  Presiona Ctrl+C para detener             ║")
print(f"╚════════════════════════════════════════════╝")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nDeteniendo servidor...")
finally:
    httpd.shutdown()
    httpd.server_close()
    print("Servidor web detenido")
