#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
from urllib.request import urlopen
import bs4

class ClientWeb(object):
    """docstringlientWeb."""
    def __init__(self):
        super(ClientWeb, self).__init__()
        pass

    def descarregar_html(arg):
        f = urllib2.urlopen("http://www.eps.udl.cat/ca/")
        html = f.read()
        f.close()
        return html

    def buscar_activitats(self, html):
        arbre = bs4. BeautifulSoup(html, features="lxml")
        activitats = arbre.find_all("div","featured-links-item")


    def run(self):
        html = self.descarregar_html()
        print(html)


if __name__ == "--main__":
    c = ClientWeb()
    c.run()


# decarregar-me html
#buscar activitats
#imprimir resultats
