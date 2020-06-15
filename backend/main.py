from bottle import route, run, template
from bottle import static_file


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/path/to/your/static/files')


@route('/')
def index():
    return '<b>Hello world</b>!'

if __name__=='__main__':
    run()