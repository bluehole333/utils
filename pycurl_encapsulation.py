import pycurl


def _call(resource, method, data=None, headers=None, timeout=None, debug=None):
    method = method.upper()
    handle = pycurl.Curl()
    output = StringIO()

    handle.setopt(pycurl.URL, resource)
    handle.setopt(pycurl.SSL_VERIFYPEER, 0)

    if headers:
        handle.setopt(pycurl.HTTPHEADER, ['%s: %s' % (
            header, str(value)) for header, value in headers.iteritems()])

    if timeout:
        handle.setopt(pycurl.TIMEOUT, timeout)

    if debug:
        handle.setopt(pycurl.VERBOSE, True)

    if method == 'POST':
        handle.setopt(pycurl.POST, True)
        handle.setopt(pycurl.POSTFIELDS, data)
    elif method == 'PUT':
        handle.setopt(pycurl.PUT, True)
        handle.setopt(pycurl.READFUNCTION, StringIO(data).read)
    elif method == 'DELETE':
        handle.setopt(pycurl.CUSTOMREQUEST, 'DELETE')

    handle.setopt(pycurl.WRITEFUNCTION, output.write)
    handle.perform()

    code = handle.getinfo(pycurl.RESPONSE_CODE)
    response = output.getvalue()

    return code, response


def post(resource, data=None, headers=None, timeout=None, debug=None):
    """HTTP POST using pycurl"""
    return _call(resource, 'POST', data=data, headers=headers, timeout=timeout, debug=debug)


def get(resource, headers=None, timeout=None, debug=None):
    """HTTP GET using pycurl"""
    return _call(resource, 'GET', headers=headers, timeout=timeout, debug=debug)
