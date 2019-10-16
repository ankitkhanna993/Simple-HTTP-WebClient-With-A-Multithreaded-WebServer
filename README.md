Simple-Http-Web-Client-Server
-----------
A Python implementation of Simple HTTP Web Client and a Multithreaded Web Server.

###Development Tools:    
1. **Programming Language:** Python3
2. **IDE:** PyCharm (Community Edition 2019.1)
3. **OS:** MacOS Mojave
4. **Command Line Interface:** MacOS Terminal (Unix)

###File Structure
1. **server.py:**    
    * Initializes the WebServer at port 6789.
    * Implements a multithreaded server and initializes a serverSocket to listen to the client requests.

2. **client.py:**
    * Implements a simple web client which communicates with the server on a specific ip:port(localhost:6789) and requests a file(HelloWorld.html) on the server.

3. **index.html:**
    * A default html file which is sent to the client in case a GET request contains "/" or empty filepath.

###Compile & Run Instructions (Run on MacOS Terminal):
1. Run Server file using:    
    `python server.py`

2. Run Client file using:  
    a. Browser: `localhost:6789/HelloWorld.html` or `localhost:6789/`
    
	b. Terminal: `python client.py localhost 6789 HelloWorld.html`
	or     
	`python client.py localhost 6789 /`


3. If `file` exists on the server, the server will return a `HTTP/1.1 200 OK` response with appropriate content-type and file content. The web client will extract status line and show it on the command prompt.

4. If `file` does NOT exist on the server, the server will return a `HTTP/1.1 404 Not Found` response with a general error message.

###References
1. The  textbook, Computer Networks: A Top Down Approach, chapter 2, section 2.2.3, for details on HTTP message format and section 2.7 for socket programming.
3. Format of the HTTP GET request and response from [Wikepedia](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
4. Thread Tutorial from [Python](https://docs.python.org/2/library/multiprocessing.html)
5. Socket Programming from [Python](https://docs.python.org/2/library/socket.html)