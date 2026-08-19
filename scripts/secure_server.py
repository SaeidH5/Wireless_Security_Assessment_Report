import http.server
import ssl

server_address = ('0.0.0.0', 8443)
handler = http.server.SimpleHTTPRequestHandler

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

httpd = http.server.HTTPServer(server_address, handler)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving securely on https://10.10.0.10:8443")
try:
	httpd.serve_forever()
except KeyboardInterrupt:
	print("Server stopped.")
	httpd.server_close()
