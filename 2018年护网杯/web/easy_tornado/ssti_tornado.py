#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2018-10-15 14:34:35
"""
import tornado.ioloop
import tornado.web
import hashlib

settings = {
    "cookie_secret": 'M)Z.>}{O]lYIp(oW7$dc132uDaK<C%wqj@PA![VtR#geh9UHsbnL_+mT5N~J84*r',
    "compiled_template_cache": False,
    'autoreload': True
}

files = {
    "/welcome.txt": "render",
    "/hints.txt": "md5(cookie_secret+md5(filename))",
    "/flag.txt": "flag in /fllllllllllllag",
    "/fllllllllllllag": "flag{this_flag_for_you!}",
}


def md5(x):
    _md5 = hashlib.md5()
    _md5.update(x)
    return _md5.hexdigest()


def gen_hash(filename):
    return md5(settings['cookie_secret']+md5(filename))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(
            '<br/>'.join(
                ["<a href='/file?filename=%s&filehash=%s'>%s</a>" % (i, gen_hash(i), i) for i in files if 'lllllll' not in i]))


class FileHandler(tornado.web.RequestHandler):
    def get(self):
        filename = self.get_argument('filename', '')
        filehash = self.get_argument('filehash', '')
        for key in files:
            if filename == key and filehash == gen_hash(key):
                return self.write("%s<br>%s" % (key, files[key]))
        self.redirect("/error?msg=Error", permanent=True)


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        print(dir(self))
        msg = self.get_argument('msg', 'Error')
        bans = ["\"", "'", "[", "]", "_", "|", "import",
                "os", "(", ")", "+", "-", "*", "/", "\\", "%", "="]
        # for ban in bans:
        #     if ban in msg:
        #         self.finish("ORZ")
        with open("error.html", 'w') as f:
            f.write("""<html>
                <head>
                <style>body{font-size: 30px;}</style>
                </head>
                <body>%s</body>
                </html>\n""" % msg)
        self.render("error.html")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/file", FileHandler),
        (r"/error", ErrorHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    print("[+] http://127.0.0.1:5000/")
    tornado.ioloop.IOLoop.current().start()
