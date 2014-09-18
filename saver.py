# -*- coding: utf-8 -*-
# ===========================================================================
# Saver
# Copyright 2014 Saver (Elp Exporter from mediawiki) Vicent Fernandez i Capilla
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
from exe.engine.package import Package
from wikipediaidevicelliurex import WikipediaIdeviceLliurex

from exe.engine.node import Node
class Saver():

  def __init__(self,outputfilename="prova2.elp",titol="Exportacio de LliureX"):

    self._outputfile = outputfilename
    self._titol = titol

    self.document = Package('LLiureX')

    self.document.set_name('Lliurex')
    self.document.set_description('Lliurex')
    self.document.set_author('Lliurex')
    self.document.set_title('Documentacio LLiurex')

  def addWikipedia(self,title,url,parent):
     W = WikipediaIdeviceLliurex(url)
     W.set_title(title)
     W.edit = False
     W.loadArticle("")
     W.undo = False
     parent.addIdevice(W)

  def save(self):
    self.document.save(self._outputfile)

  def AddNode(self,parent,titol):
    Fill = parent.createChild();
    Fill.setTitle(titol)
    return Fill

  def getRoot(self):
    return self.document.root
