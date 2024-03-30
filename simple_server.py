from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# HTML content for the UI
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interactive Portfolio</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    header {
      background-color: #333;
      color: #fff;
      padding: 20px;
      text-align: center;
    }

    main {
      display: flex;
      justify-content: space-between;
      padding: 20px;
    }

    .project {
      border: 1px solid #ddd;
      border-radius: 5px;
      margin-bottom: 20px;
      padding: 20px;
      cursor: pointer;
      width: 45%;
    }

    .project:hover {
      background-color: #f9f9f9;
    }

    .project img {
      max-width: 100%;
      height: auto;
    }

    .project-content {
      display: flex;
      flex-direction: column;
    }
  </style>
</head>
<body>
  <header>
    <h1>My Portfolio</h1>
  </header>
  
 <main>
    <section class="project" id="project1">
      <div class="project-content">
        <h2>Project 1</h2>
        <p>This is me</p>
      </div>
        <img src="images/1.png" alt="Project 1 Image">
      </a>
    </section>

    <section class="project" id="project2">
      <div class="project-content">
        <h2>Project 2</h2>
        <p>This is also me</p>
      </div>
      <img src="images/2.png" alt="Project 2 Image">
    </section>
    
    <section class="project" id="project3">
      <div class="project-content">
        <h2>Project 3</h2>
        <p>this is also me but me</p>
      </div>
      <img src="images/3.png" alt="Project 3 Image">
    </section>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', function () {
      const projects = document.querySelectorAll('.project');
      
      projects.forEach(project => {
        project.addEventListener('click', function () {
          alert(`Clicked on ${project.querySelector('h2').innerText}`);
        });
      });
    });
  </script>
</body>
</html>
"""

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
        else:
            # Serve static files (images)
            try:
                with open(os.getcwd() + self.path, 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', 'image/png')  # Change the content type based on your image type
                    self.end_headers()
                    self.wfile.write(file.read())
            except IOError:
                self.send_error(404, 'File Not Found: %s' % self.path)

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server started on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
