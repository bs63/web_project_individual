#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
from urllib.request import urlopen
import bs4

class ClientWeb(object):
    """web packtpub"""
    def __init__(self):
        super(packtpub, self).__init__()
        pass

    def descarregar_html(arg):
        f = urllib2.ur
        lopen("https://www.packtpub.com/packt/offers/free-learning/")
        html = f.read()
        f.close()
        return html

    def buscar_activitats(self, html):
        arbre = bs4. BeautifulSoup(html, features="lxml")
        activitats = arbre.find_all("div","featured-links-item")
        activity_list = []
        for activity in activitats:
            title = activity.find("span", "flink-title")
            link = activity.find("a")
            activity_list.append(title.text, link["href"])
        return activitats_list



    def run(self):
        html = self.descarregar_html()
        print(html)


if __name__ == "--main__":
    c = ClientWeb()
    c.run()


# decarregar-me html
#buscar activitats
#imprimir resultats
