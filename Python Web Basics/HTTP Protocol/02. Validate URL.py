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

    required_component_names = [
        'Protocol',
        'Host',
        'Port',
        'Path',
    ]

    optional_component_names = [
        'Query',
        'Fragment',
    ]

    are_required_components_present = all(result[name] for name in required_component_names)

    if are_required_components_present:
        for component_name in required_component_names + optional_component_names:
            if result[component_name]:
                print(f'{component_name}: {result[component_name]}')
    else:
        print('Invalid URL')


validate('http://softuni.bg/')
validate('https://softuni.bg:447/search?Query=pesho&Users=true#go')
validate('http://google:443/')