import http.server
import socketserver
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Set the uncommon port number you want to use
PORT = 9999

# Define the directory where uploaded files will be saved
UPLOAD_DIR = "./uploaded_files"

# Create the upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Define a request handler class
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Add custom logic if needed
        super().do_GET()

    def do_POST(self):
        # Handle POST requests (file uploads)
        content_length = int(self.headers['Content-Length'])
        uploaded_file = self.rfile.read(content_length)
        filename = os.path.join(UPLOAD_DIR, self.path.lstrip("/"))

        with open(filename, 'wb') as f:
            f.write(uploaded_file)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'File uploaded successfully!')

# Create a socket server with the specified port and request handler
httpd = socketserver.TCPServer(("", PORT), MyRequestHandler)

# Create a Tkinter window
window = tk.Tk()
window.title("Local Server Info")
window.geometry("400x300")  # Set the window size

# Create and pack labels to display server information
server_info_label = tk.Label(window, text=f"Server running on port {PORT}", font=("Helvetica", 14))
server_info_label.pack(pady=20)

# Function to display a message box with server status
def show_server_status():
    messagebox.showinfo("Server Status", f"The server is running on port {PORT}")

# Create and pack a button to show server status
status_button = tk.Button(window, text="Check Server Status", command=show_server_status, font=("Helvetica", 12))
status_button.pack()

# Function to handle file upload
def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        url = f"http://localhost:{PORT}/{file_name}"
        messagebox.showinfo("File Uploaded", f"File '{file_name}' uploaded successfully.\nURL: {url}")

# Create and pack a button to upload files
upload_button = tk.Button(window, text="Upload File", command=upload_file, font=("Helvetica", 12))
upload_button.pack()

# Start the server in a separate thread
def start_server():
    print(f"Server started on port {PORT}")
    httpd.serve_forever()

import threading
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Run the Tkinter event loop
window.mainloop()
