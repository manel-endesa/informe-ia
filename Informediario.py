
# Agente IA para interpretar incidencias operativas en texto narrativo.
# 
# Entrada: texto libre (ejemplo: incidentes SAP, lentitud, en análisis, mismo estado que ayer...)
#
# Salida:
# - Incidencia (resumen corto)
# - Impacto (efecto en negocio/sistemas)
# - Estado (en análisis, resuelto, sin cambios...)
# - Resumen ejecutivo claro
#
# El agente debe interpretar lenguaje natural como lo haría un responsable de operaciones.


from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/generar":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            texto = data.get("texto", "")

            respuesta = {
                "Incidencia": "Sistema no disponible",
                "Impacto": "Usuarios no pueden operar",
                "CausaRaiz": "Pendiente de análisis",
                "ProximosPasos": "Revisión del equipo técnico",
                "TextoOriginal": texto,
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(respuesta, ensure_ascii=False).encode('utf-8'))

server = HTTPServer(('localhost', 8000), MyHandler)
print("Servidor corriendo en http://localhost:8000")
server.serve_forever()
