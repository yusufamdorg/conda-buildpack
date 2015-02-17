from __future__ import print_function
import os
import sys

print(os.environ)
for a in os.environ["PYTHONPATH"].split(":"):
    print("%s exists? %s" % (a, os.path.exists(a)))

from werkzeug.wrappers import Request, Response

name = "World" if len(sys.argv) == 1 else sys.argv[1]


@Request.application
def application(request):
    return Response('Hello, {}!'.format(name))

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
