# -- coding: utf-8 --
# ===========================================================================
# eXe
# Copyright 2004-2006, University of Auckland
# Copyright 2006-2008 eXe Project, http://eXeLearning.org/
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

"""
A Wikipedia Idevice is one built from a Wikipedia article.
"""

import re
from exe.engine.wikipediaidevice import WikipediaIdevice
import urllib
from exe.engine.beautifulsoup import BeautifulSoup, Comment
from exe.engine.path          import Path, TempDirPath
from exe.engine.resource      import Resource
# ===========================================================================
class WikipediaIdeviceLliurex(WikipediaIdevice):
    lliurexWikiUrl = "http://10.0.0.172"
    def loadArticle(self, name):
        """
        Load the article from Wikipedia
        """
        self.articleName = name
        url = ""
        name = urllib.quote(name.replace(" ", "_").encode('utf-8'))
        try:
            url  = (self.site or self.ownUrl)
            if not url.endswith('/') and name <> '': url += '/'
            if '://' not in url: url = 'http://' + url
            url = url.replace(" ","_")
            url = url.encode('utf-8')
            url += name
            net  = urllib.urlopen(url)
            page = net.read()
            net.close()
        except IOError, error:
            log.warning(unicode(error))
            self.article.content = _(u"Unable to download from %s <br/>Please check the spelling and connection and try again.") % url
            self.article.content_w_resourcePaths = self.article.content
            self.article.content_wo_resourcePaths = self.article.content
            return

        page = unicode(page, "utf8")
        # FIXME avoid problems with numeric entities in attributes
        page = page.replace(u'&#160;', u'&nbsp;')
        # avoidParserProblems is set to False because BeautifulSoup's
        # cleanup was causing a "concatenating Null+Str" error,
        # and Wikipedia's HTML doesn't need cleaning up.
        # BeautifulSoup is faster this way too.
        soup = BeautifulSoup(page, False)
        content = soup.first('div', {'id': "content"})
        #content = soup.div(id="content")
        #Fix bug #1359: El estilo ITE no respeta ancho de página al exportar
        #a páginas web si se usa iDevice wikipedia
        #import pprint
        #pprint.pprint(content)
        #content['id'] = "wikipedia-content"

        # remove the wiktionary, wikimedia commons, and categories boxes
        #  and the protected icon and the needs citations box
        if content:
            content['id'] = "wikipedia-content"
            infoboxes = content.findAll('div',
                    {'class' : 'infobox sisterproject'})
            [infobox.extract() for infobox in infoboxes]
            catboxes = content.findAll('div', {'id' : 'catlinks'})
            [catbox.extract() for catbox in catboxes]
            amboxes = content.findAll('table',
                    {'class' : re.compile(r'.*\bambox\b.*')})
            [ambox.extract() for ambox in amboxes]
            protecteds = content.findAll('div', {'id' : 'protected-icon'})
            [protected.extract() for protected in protecteds]
            # Extract HTML comments
            comments = content.findAll(text=lambda text:isinstance(text, Comment))
            [comment.extract() for comment in comments]
        else:
            content = soup.first('body')

        if not content:
            log.error("no content")
            self.article.content = _(u"Unable to download from %s <br/>Please check the spelling and connection and try again.") % url
            # set the other elements as well
            self.article.content_w_resourcePaths = self.article.content
            self.article.content_wo_resourcePaths = self.article.content
            return

        # clear out any old images
        while self.userResources:
            self.userResources[0].delete()
        self.images        = {}

        # Download the images
        bits = url.split('/')
        netloc = '%s//%s' % (bits[0], bits[2])
        path = '/'.join(bits[3:-1])
        tmpDir = TempDirPath()
        for imageTag in content.fetch('img'):
            imageSrc  = unicode(imageTag['src'])
            imageName = imageSrc.split('/')[-1]
            imageName = imageName.replace('&gt;', '>')
            imageName = imageName.replace('&lt;', '<')
            imageName = imageName.replace('&quot;', '"')
            imageName = imageName.replace('&nbsp;', '')
            imageName = imageName.replace('%2C', ',')
            imageName = imageName.replace('%22', '"')
            imageName = imageName.replace('%28', '(')
            imageName = imageName.replace('%29', ')')
            imageName = imageName.replace('%C3%A5', 'å')
            #JR: decodificamos el nombre de la imagen
            imageName = urllib.unquote(imageName)
            # Search if we've already got this image
            imageSrc = self.lliurexWikiUrl + imageSrc
            imageName = imageName.encode('ascii', 'ignore')
            urllib.urlretrieve(imageSrc, tmpDir/imageName)
            new_resource = Resource(self, tmpDir/imageName)
            self.images[imageName] = True
            #imageTag['src'] = (u"resources/" + imageName)
            imageTag['src'] = (imageSrc)
        self.article.content = self.reformatArticle(netloc, unicode(content))
        #print self.article.content
        # now that these are supporting images, any direct manipulation
        # of the content field must also store this updated information
        # into the other corresponding fields of TextAreaField:
        # (perhaps eventually a property should be made for TextAreaField
        #  such that these extra set's are not necessary, but for now, here:)
        self.article.content_w_resourcePaths = self.article.content
        self.article.content_wo_resourcePaths = self.article.content
