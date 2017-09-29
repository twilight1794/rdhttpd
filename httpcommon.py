#

class httpreq(object):
    '''Base class for any HTTP request'''
    def __init__(self):
        self.rawrequest = ""
        self.headerlines = {
            "requestLine": ""
       }
    def parse(self, req):
        '''Accepts a string containing a raw HTTP request (as sended by the client, but converted to string)
        Returns a dictionary where the key is the header name, and the value is the header value
        The first key is called "requestLine", and contains a tuple with 3 items: method, requested resource, and HTTP version,'''
        self.rawrequest = req
        listrequest = self.rawrequest.splitlines().pop()
        i = 1  # Number of Iteration
        for string in listrequest:
            if i == 1:
                self.headerlines.setdefault("requestLine", string)
            else:
                stringtuple = string.split(": ")
                self.headerlines.setdefault(stringtuple[0], stringtuple[1])
            i += 1
        return self.headerlines

class httpresp(object):
    '''Base class for any HTTP response'''
    def __init__(self):
        self.content = ""
        self.header = {
            "statusLine": "",
        }
        self.header["statusLine"] = "HTTP 1.0 200 OK"
    def setHeader(self, headern, value):
        self.header.setdefault(headern, value)
        return str(headern) + str(value)
    def rmHeader(self, headern):
        del(self.header[headern])
        return str(headern)
    def __str__(self):
        string = ""
        i = 1
        for key, value in self.header.items():
            if i == 1:
                string += str(value) + "\r\n"
            else:
                string += str(key) + str(value) + "\r\n"
            i += 1
        string += "\r\n"
        string += self.content
        return string

def getFileRequested(filer): # In rev
    '''This function returns the file passed by parameter. First, check the list of available CGIs. If the file requested is on that list, will be execute the CGI and will return the result. Otherwise, will be served the file directly.'''
    if filer in cgilist:
        try:
            importlib.import_module(filer)
        except ImportError:
            raise ImportError("The CGI isn't available")
    else:
        try:
            filerequested = open(filer, "rb")
            return filerequested.read()
        except:
            raise RuntimeError("The file isn't available")
        finally:
            filerequested.close()

class HTTPRespCode(object):
    """A class that manages all related about HTTP status codes"""
    def __init__(self, code):
        try:
            for i in httpconst.statuscodes:
                if str(code) == i[0]:
                    self.code = i[0]
                    self.strcode = i[0] + " " + i[1]
                    break
                else:
                    continue
            len(self.code)
        except AttributeError:
            raise ValueError("The parameter must be an valid HTTP status code")
    def __str__(self):
        return self.strcode


class HTTPHeaders(object):
    def __init__(self):
        pass


class HTTPPercentEntities(object):
    def __init__(self):
        pass


class HTTPTime(object):
    """A class that manages all related about HTTP Time"""
    def __init__(self):
        from datetime import datetime
        time = datetime.today()
        self.time = time.utcnow()
    def date822(self):
        """Returns the date as described on RFC 822 (updated by RFC 1123)
        Ex: Sun, 06 Nov 1994 08:49:37 GMT"""
        mask = "%a, %d %b %Y %H:%M:%S GMT"
        return self.time.strftime(mask)
    def date850(self):
        """Returns the date as described on RFC 850 (obsoleted by RFC 1036)
        Ex: Sunday, 06-Nov-94 08:49:37 GMT"""
        mask = "%A, %d-%b-%y %H:%M:%S GMT"
        return self.time.strftime(mask)
    def dateANSI(self):
        """Returns the date as the ANSI C's asctime() format
        Ex: Sun Nov  6 08:49:37 1994"""
        mask = "%a %b  %d %H:%M:%S %Y"
        return self.time.strftime(mask)


class QualityValues(object):
    """A class that manages all related about q=* values"""
    qdict = {} # The dictionary of q=* values

    def __init__(self, param):
        """param -> A string that contains the request
        Ex: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"""
        for i in param.split(","):
            if re.match("[A-Za-z/\*]*(;q=)+[0-9\.]*", i):
                temp = i.partition(";q=") #  temp[0]: The TypeMIME (or MIMEType???); temp[1]: The string ";q="; temp[2]: The q value
                if self.QMatchs(temp[2]) == True:
                    self.qdict[temp[0]] = temp[2]
                else:
                    self.qdict[temp[0]] = float(1.000)
            else:
                self.qdict[i] = float(1.000)

    def QMatchs(self, val):
        """Checks if the parameter passed is a valid quality value"""
        regexp = "0(\.[0-9]{1,3})*|1(\.0{1,3})*" # I could use this regex, substituting the two previous regexes: [A-Za-z/\-\*]*(;q=)(0(\.[0-9]{1,3})*|1(\.0{1,3})*)*
        if re.match(regexp, val):
            return True
        else:
            return False


class HTTPCompression(object):
    """A class that manages all related about HTTP compression"""
    acceptFormats = ("gzip", "compress", "deflate", "identity")


class MediaTypes(object):
    acceptFormats = ()


class LangTags(object):
    pass
