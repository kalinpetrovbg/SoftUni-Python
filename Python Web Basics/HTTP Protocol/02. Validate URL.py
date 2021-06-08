from urllib import parse

def get_protocol(scheme):
    if scheme in ('http', 'https'):
        return scheme

def get_host(netloc):
    if '.' not in netloc:
        return
    elif ':' in netloc:
        return netloc.split(':')[0]
    return netloc

def get_port(netloc, scheme):
    if ':' in netloc:
        return netloc.split(':')[1]
    if scheme == 'http':
        return 80
    elif scheme == 'https':
        return 443

def get_path(path):
    return path or '/'


def validate(url):
    data = parse.urlparse(url)

    result = {
        'Protocol': get_protocol(data.scheme),
        'Host': get_host(data.netloc),
        'Port': get_port(data.netloc, data.scheme),
        'Path': get_path(data.path),
        'Query': data.query,
        'Fragment': data.fragment,
    }

    return result


print(validate('http://softuni.bg/'))
print(validate('https://softuni.bg:447/search?Query=pesho&Users=true#go'))
print(validate('http://google:443/'))