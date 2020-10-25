# This work is licensed by Zachary J. Szewczyk under the Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License. See
# http://creativecommons.org/licenses/by-nc-sa/4.0/ for more information.

# Imports
from urllib.request import Request, build_opener, HTTPCookieProcessor # Building and executing web requests.
from http.cookiejar import CookieJar # Handling cookies
from urllib.error import URLError, HTTPError # Catching errors
from html import unescape # Parsing title elements
from random import choice # Choosing random user agent string
from gzip import decompress # Handling gzip compressed pages
from os.path import isfile # User agent string file check

# Class: Web
# Purpose: Provide a high-level interface for interacting with web endpoints.
class Web():
    # Method: __init__
    # Purpose: Define variables for web request interface.
    # Parameters:
    # - self: Class reference (Object)
    # Return: none.
    def __init__(self):
        # Define headers
        self.headers = {
            # https://oxylabs.io/blog/5-key-http-headers-for-web-scraping
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", # Accepted data formats
            "Accept-Encoding":"gzip", # Accepted encodings
            "Accept-Language":"en-US,en;q=0.5", # Accepted languages
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "DNT":"1",
            "Pragma":"no-cache",
            "Upgrade-Insecure-Requests":"1",
            "Referer":"http://www.google.com/" # Referring web page
        }

        # Try to read a file of common user agent strings, culled from
        # https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/
        if (isfile("./user_agents.txt")):
            fd = open("./User_agents.txt", "r")
            self.user_agent_pool = fd.read().split('\n')
            fd.close()
            # Append random user agent string to headers from agent pool
            self.headers["User-Agent"] = choice(self.user_agent_pool)
        else:
            self.headers["User-Agent"] = "Mozilla/5.0 Gecko Firefox"

        # Define request timeout, in seconds
        self.timeout = 10

        # Store last request response
        self.url = ""
        self.data = ""

    # Method: retrieve
    # Purpose: Use the specified HTTP method, optional extra headers,
    # and optional request body to retrieve the data at the given URL.
    # Parameters:
    # - url: Target URL (String)
    # - headers: Optional additional request headers (Dict)
    # - method: HTTP request method (String)
    # - data: HTTP request body (String)
    # Return:
    # - Success: HTTP response code if 200 <= code < 400 (Int)
    # - Failure: 0 if 0 < code < 200 or 400 <= code <= 599 (Int)
    def retrieve(self,url,headers,method,data):
        # Update the last requested URL and response data
        self.url = url
        self.data = ""

        # Define the request
        request = Request(url, headers=self.headers, method=method, data=data)

        # Add provided headers
        if (headers != {}):
            for key,value in headers.items():
                request.add_header(key,value)

        # Instantiate a cookie jar to handle sites that require cookies
        cj = CookieJar()

        # Try to make the request, and handle a subset of likely errors.
        try: response = build_opener(HTTPCookieProcessor(cj)).open(request, timeout=self.timeout)
        # Handle typical HTTP errors (i.e. 404: Not Found) by reading the 
        # response page's content.
        except HTTPError as e: response = e
        # If the error is that the certificate cannot be verified, try to
        # read the page without certificate verification.
        except URLError as e:
            if ("CERTIFICATE_VERIFY_FAILED" in str(e.reason)):
                import ssl
                ssl._create_default_https_context = ssl._create_unverified_context
                try: response = build_opener(HTTPCookieProcessor(cj)).open(request, timeout=self.timeout)
                except: return 0
            # If it's not a 404 error, and not failure to verify a 
            # certificate just return 0 to indicate failure.
            else: return 0

        # Parse response headers into key-value dictionary
        response_headers = {x[0].lower():x[1] for x in response.getheaders()}

        # Handle response content encoding.
        if ("content-encoding" in response_headers.keys()):
            if (response_headers["content-encoding"] == "gzip"):
                data = decompress(response.read())
            else: data = response.read()
        else:
            data = response.read()
    
        if ("content-type" in response_headers.keys()):
            if ("zip" in response_headers["content-type"]):
                self.data = data
            else:
                # Try to decode
                try: self.data = data.decode("utf-8")
                except: self.data = repr(data) 
        else:
            # Try to decode
            try: self.data = data.decode("utf-8")
            except: self.data = repr(data) 
        
        # Finally, return the response code.
        return response.code

    # Method: get
    # Purpose: Helper method to retrieve data at URL with a GET request, using
    # optional additional headers.
    # Parameters:
    # - url: Target URL (String)
    # - headers: Optional additional request headers (Dict)
    # Return:
    # - Success: HTTP response code if 200 <= code < 400 (Int)
    # - Failure: 0 if 0 < code < 200 or 400 <= code <= 599 (Int)
    def get(self,url,headers={}):
        return self.retrieve(url,headers,"GET",data=None)

    # Method: post
    # Purpose: Helper method to POST data to URL with a POST request, using
    # optional additional headers.
    # Parameters:
    # - url: Target URL (String)
    # - headers: Optional additional request headers (Dict)
    # - data: Data to post (Bytes)
    # Return:
    # - Success: HTTP response code if 200 <= code < 400 (Int)
    # - Failure: 0 if 0 < code < 200 or 400 <= code <= 599 (Int)
    def post(self,url,headers,data):
        return self.retrieve(url,headers,"POST",data)

    # Method: get_data
    # Purpose: Get response data from the most recent request
    # Parameters:
    # - self: Class reference (Object)
    # Return: Response data from most recent request (String)
    def get_data(self):
        return self.data

    # Method: get_url
    # Purpose: Get the URL from the most recent request
    # Parameters:
    # - self: Class reference (Object)
    # Return: URL from most recent request (String)
    def get_url(self):
        return self.url

    # Method: get_title
    # Purpose: Get the page title for the most recent request
    # Parameters:
    # - self: Class reference (Object)
    # Return: Page title from most recent request, or its URL (String)
    def get_title(self):
        # If the most recent request failed, return the request URL.
        if (self.data == ""):
            return self.url

        # Site-specific title parsing
        if (any([x in self.url for x in ["youtube.com", "youtu.be"]])): # YouTube.com
            start = self.data.find(r'<meta property="og:title"')
            title = self.data[start:].split('\n')[0]
            title = title.split('content="')[1][:-2].strip()
        elif ("twitter.com" in self.url): # Twitter.com
            return self.url # All JavaScript, so just return the URL.
        else:
            # Find <title and </title.
            start = self.data.lower().find("<title")
            end = self.data.lower().find("</title")
            
            # Some pages just won't have a title. Account for this.
            if (start == -1 or end == -1):
                return self.url

            # Extract the full <title> element
            title = self.data[start:end]

            # Strip opening title tag
            title = title.split(">",1)[1]

        # Transform escaped HTML entitites, and strip whitespace
        title = unescape(title).strip()

        # There may be lingering control characters, so deal with those
        title = title.replace(r'\n','').replace(r'\r','')

        # Return parsed title
        return title

    # Method: save_as
    # Purpose: Save response data in a local file.
    # Parameters:
    # - self: Class reference (Object)
    # - file: Path to output file (String)
    # Return: True (File write succeeds); False (File write fails)
    def save_as(self, file):
        # Only permit saving in or below the current directory
        if (file[0:1] != "./"): file = "./"+file

        # Write the response data to the file, and catch the error.
        try:
            fd = open(file, "w")
            fd.write(self.get_data())
            fd.close()
            return True
        except:
            return False

    # Method: get_user_agents
    # Purpose: Retrieve a list of 50 common user agents to store locally.
    # Parameters:
    # - self: Class reference (Object)
    # Return: None
    def get_user_agents(self):
        # Clear and open the output file, ./user_agents.txt
        open("./user_agents.txt", "w").close()
        fd = open("./user_agents.txt", "a")

        # Retrieve the list of user agent strings from whatismybrowser.com
        w = Web()
        w.get("https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/")
        
        # Extract the top 50 user agent strings
        e = enumerate(w.get_data().split('\n'))
        for i,line in e:
            if ("<tr>" in line):
                i,line = next(e)
                if ("<a" in line):
                    fd.write(line.split(">",2)[2][:-9]+'\n')

        # Close the file
        fd.close()

# If run as a standalone program, do nothing.
if (__name__ == "__main__"):
    pass
