
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# ===========================================================================
# Runer (Exemple of use)
# Copyright 2014 Run (Elp Exporter from mediawiki) Vicent Fernandez i Capilla
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


from loader import Loader
from saver import Saver
from exe.engine.node import Node
import sys
import os
class Run:
  @staticmethod
  def  process():
    arxiu = sys.argv[1]
    os.environ["HOME"] = "/var/www"
    L = Loader(arxiu + ".txt")
    S = Saver(arxiu + ".elp",L._title)
    N = S.getRoot()    
    for T in L.Temes:
      Pare = S.AddNode(N, T.title)
      for W in T.llistaItems:
        S.addWikipedia(W.title,W.url,Pare)
    S.save()
Run.process()
