from urllib import parse

def get_protocol(scheme):
    pass

def get_host(netloc):
    pass

def get_port(netloc, scheme):
    pass

def get_path(path):
    pass


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


print(validate('http://softuni.bg/'))
print(validate('https://softuni.bg:447/search?Query=pesho&Users=true#go'))
print(validate('http://google:443/'))