from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
     <head>
          <title>THE BEST 2021 SOFTWARE IPO</title>
     </head>
     <body>
     <table border="4" cellspacing="5" cellpadding="5" width="40" height="50">
     <caption> Only CFO's Newsletter
        <tr>
			<th>Rank</th>
			<th>Name</th>
			<th>Rev</th>
            <th>FCP</th>
            <th>Growth</th>
            <th>Margin</th>
		</tr>
        <tr>
			<td>1</td>
			<td>Snowflake</td>
			<td>17.6x</td>
			<td>63x</td>
            <td>27%</td>
            <td>66%</td>
        </tr>
        <tr>
			<td>2</td>
			<td>MongoDB</td>
			<td>17.7x</td>
			<td>150x</td>
            <td>17%</td>
            <td>74%</td>
        </tr>
        <tr>
			<td>3</td>
			<td>Cloudflare</td>
			<td>16.7x</td>
			<td>193x</td>
            <td>28%</td>
            <td>76%</td>
        </tr>
        <tr>
			<td>4</td>
			<td>Palantir</td>
			<td>16.1x</td>
			<td>64x</td>
            <td>19%</td>
            <td>80%</td>
        </tr>
        <tr>
			<td>5</td>
			<td>DataDoge</td>
			<td>15.1x</td>
			<td>60x</td>
            <td>21%</td>
            <td>80%</td>
        </tr>
    </table>
	</body>
</html>

	


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()