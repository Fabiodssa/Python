import http.server
import socketserver
from urllib.parse import parse_qs

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Ler o conteúdo do formulário enviado
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        dados = parse_qs(post_data)

        # Extrair valores
        try:
            n1 = float(dados['n1'][0])
            n2 = float(dados['n2'][0])
            op = dados['operacao'][0]
            
            if op == '+': res = n1 + n2
            elif op == '-': res = n1 - n2
            elif op == '*': res = n1 * n2
            elif op == '/': res = n1 / n2 if n2 != 0 else "Erro: Divisão por 0"
        except:
            res = "Erro nos dados"

        # Responder ao navegador com o resultado
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        response = f"<html><body><h1>Resultado: {res}</h1><a href='/'>Voltar</a></body></html>"
        self.wfile.write(response.encode('utf-8'))

    def do_GET(self):
        # Serve o arquivo index.html quando acessamos a página
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Iniciar o servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando em http://localhost:{PORT}")
    httpd.serve_forever()