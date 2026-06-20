from http.server import BaseHTTPRequestHandler, HTTPServer
import psutil
import json
import platform
import socket
import time
class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
#Server Check(Verified)
		if self.path=="/":
			self.send_response(200)
			self.send_header("Content-type","text/plain")
			self.end_headers()
			self.wfile.write(b"Server is running")
#Computer Info(Verified)
		elif self.path=="/status":
			data={
				"cpu":psutil.cpu_percent(interval=1),
				"ram":psutil.virtual_memory().percent,
				"disk":psutil.disk_usage("/").percent
			}

			self.send_response(200)
			self.send_header("Content-type", "application/json")
			self.end_headers()
			self.wfile.write(json.dumps(data).encode())
#Health Check(Verified)
		elif self.path=="/health":
			cpu=psutil.cpu_percent()
			ram=psutil.virtual_memory().percent
			disk=psutil.disk_usage('/').percent
			status="HEALTHY"
			if cpu>90 or ram > 95 or disk > 95:
				status="UNHEALTHY"
			reasons=[]
			if cpu>90:
				reasons.append(" CPU usage critical ")
			if ram>95:
				reasons.append(" RAM usage critical ")
			if disk>95:
				reasons.append("Disk usage critical")
			self.send_response(200)
			self.send_header("Content-type","application/json")
			self.end_headers()

			data={
				"status":status,
				"cpu_percent":cpu,
				"ram_percent":ram,
				"disk_percent":disk,
				"reasons":reasons
			}

			self.wfile.write(json.dumps(data).encode())
#Info(Verified)
		elif self.path=='/info':
			data={
				"system":platform.system(),
				"release":platform.release(),
				"hostname":socket.gethostname(),
				"boot_time":time.ctime(psutil.boot_time())
			}

			self.send_response(200)
			self.send_header("Content-type", "application/json")
			self.end_headers()
			self.wfile.write(json.dumps(data).encode())
#Top 10 Processes(Verified)
		elif self.path=="/processes":
			for proc in psutil.process_iter():
				try:
					proc.cpu_percent(None)
				except:
					pass
			time.sleep(1)
			processes=[]
			for proc in psutil.process_iter(['pid','name','cpu_percent']):
				try:
					processes.append(proc.info)
				except:
					pass
			processes.sort(
				key=lambda x: x['cpu_percent'],
				reverse=True
			)
			processes=processes[:10]
			self.send_response(200)
			self.send_header('Content-type', 'application/json')
			self.end_headers()

			self.wfile.write(json.dumps(processes).encode())
#Server Down
		else:
			self.send_response(404)
			self.end_headers()

server=HTTPServer(("0.0.0.0", 8000), Handler)

print("Server running on port 8000")
server.serve_forever()
