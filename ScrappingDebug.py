import requests
from bs4 import BeautifulSoup

# Usage
url = 'https://www.barrons.com/articles/amazon-stock-price-apple-ai-spending-0b4b25e0'

response = requests.get(url)

if response.text.__contains__("403" or "50") :
    print(response.text)
    
if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    print(f'Title of the page: {title}')
    
    
    # Extract all paragraph texts
    paragraphs = soup.find_all('script')
    texts = [p.text for p in paragraphs]
    
    print(texts)


# #
# HTTP status codes are three-digit numbers returned by a server in response to a client's request. 
# They indicate the outcome of the request and are grouped into five classes. Here's an overview of the main 
# HTTP status code categories and some common codes:
# 1xx: Informational
# These codes indicate that the request was received and the process is continuing.
# 100 Continue
# 101 Switching Protocols
# 2xx: Success
# These codes indicate that the request was successfully received, understood, and accepted.
# 200 OK
# 201 Created
# 204 No Content
# 206 Partial Content
# 3xx: Redirection
# These codes indicate that further action needs to be taken to complete the request.
# 301 Moved Permanently
# 302 Found
# 304 Not Modified
# 307 Temporary Redirect
# 308 Permanent Redirect
# 4xx: Client Error
# These codes indicate that there was an error on the client side.
# 400 Bad Request
# 401 Unauthorized
# 403 Forbidden
# 404 Not Found
# 405 Method Not Allowed
# 409 Conflict
# 413 Payload Too Large
# 429 Too Many Requests
# 5xx: Server Error
# These codes indicate that the server failed to fulfill a valid request.
# 500 Internal Server Error
# 501 Not Implemented
# 502 Bad Gateway
# 503 Service Unavailable
# 504 Gateway Timeout
# Common Error Codes Explained
# 400 Bad Request
# The server cannot process the request due to a client error (e.g., malformed request syntax)1.
# 401 Unauthorized
# The request lacks valid authentication credentials for the target resource1.
# 403 Forbidden
# The server understood the request but refuses to authorize it1.
# 404 Not Found
# The server can't find the requested resource. This is often used when the requested page or 
# file doesn't exist1.
# 500 Internal Server Error
# A generic error message when an unexpected condition was encountered and no more specific message 
# is suitable3.
# 503 Service Unavailable
# The server is not ready to handle the request. Common causes are a server that is down 
# for maintenance or that is overloaded3.
# When troubleshooting, these status codes can provide valuable information about what 
# went wrong with a request. For developers and system administrators, understanding these codes is crucial 
# for diagnosing and resolving issues in web applications and services.