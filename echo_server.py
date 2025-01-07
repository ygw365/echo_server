from http.server import BaseHTTPRequestHandler, HTTPServer

# 定义一个继承自 BaseHTTPRequestHandler 的请求处理类
class EchoHandler(BaseHTTPRequestHandler):
    # 处理 GET 请求
    def do_GET(self):
        # 发送 200 OK 响应
        self.send_response(200)
        # 设置内容类型为纯文本
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # 写入响应主体
        self.wfile.write(f"GET request for {self.path}\n".encode())
        
    # 处理 POST 请求
    def do_POST(self):
        # 确定传入数据的长度
        content_length = int(self.headers['Content-Length'])
        # 读取传入数据
        post_data = self.rfile.read(content_length)
        
        # 发送 200 OK 响应
        self.send_response(200)
        # 设置内容类型为纯文本
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # 写入响应主体
        self.wfile.write(f"POST request for {self.path}\n".encode())
        self.wfile.write(b"Received data:\n")
        self.wfile.write(post_data)

# 运行服务器的函数
def run(server_class=HTTPServer, handler_class=EchoHandler, port=4000):
    # 定义服务器地址和端口
    server_address = ('0.0.0.0', port)
    # 创建 HTTP 服务器实例
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    # 无限期运行服务器
    httpd.serve_forever()

# 脚本的入口点
if __name__ == '__main__':
    run()