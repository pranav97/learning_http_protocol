from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi


# These request verbs are:

# GET: fetch an existing resource. The URL contains all the necessary information the server needs to locate and return the resource.
# POST: create a new resource. POST requests usually carry a payload that specifies the data for the new resource.
# PUT: update an existing resource. The payload may contain the updated data for the resource.
# DELETE: delete an existing resource.


class webserverHandler(BaseHTTPRequestHandler):
     def do_GET(self):
        try:
            if self.path.endswith("/get_testing"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                output = """Hello"""
                self.wfile.write(output)
                return
        except:
            pass


def main():
    """
    what port to listen in
    """
    try:
        port = 3000
        server = HTTPServer(('', port), webserverHandler)
        print("Webserver running on port {}".format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print("^c entered, stopping")
        server.socket.close()


if __name__ == "__main__":
    main()
