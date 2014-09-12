# -*- coding: utf-8 -*-
# ===========================================================================
# Loader
# Copyright 2014 Loader (Elp Exporter from mediawiki) Vicent Fernandez i Capilla
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# ===========================================================================

import json

class wikiItem:
  title = ""
  url = ""
  def __init__ (self,Title,Url):
    self.title = Title
    self.url = Url
class TemaItem:
  title = ""
  llistaItems = []
  def __init__(self,Title=""):
    self.title = Title

class Loader:

  Temes = []
  _inputfilename = ""
  _isLoaded = False
  _title = ""
  def __init__(self, inputfilename):
    self._inputfilename = inputfilename
    self.load()

  def load(self):
    s = open(self._inputfilename).read()
    x = json.loads(s)
    self._title = x["title"]
    for capitol in x["items"]:
      T = TemaItem(capitol["title"])
      #evitar que la llista siga variable estatica, ya que si no s'assigna valor
      #totes els variables en python ho son
      T.llistaItems = []
      for pagina in capitol["items"]:
        W = wikiItem(pagina["title"],pagina["url"])
        T.llistaItems.append(W)
      self.Temes.append(T)
    self._isLoaded = True

  def process(self):
    if not self._isLoaded:
      self.load()
