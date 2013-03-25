# This file is part of Booktype.
# Copyright (c) 2012 Aleksandar Erkalovic <aleksandar.erkalovic@sourcefabric.org>
#
# Booktype is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Booktype is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Booktype.  If not, see <http://www.gnu.org/licenses/>.

import os

PUBLISH_OPTIONS =  ['book', 'bookjs', 'ebook', 'pdf', 'odt']

OBJAVI_URL =  "http://objavi.booktype.pro/objavi.cgi"
ESPRI_URL = "http://objavi.booktype.pro/espri.cgi"

THIS_BOOKI_SERVER = os.environ.get('HTTP_HOST', 'booktype-demo.sourcefabric.org')

CREATE_BOOK_VISIBLE = True
CREATE_BOOK_LICENSE = ""

FREE_REGISTRATION = True
ADMIN_CREATE_BOOKS = False
ADMIN_IMPORT_BOOKS = False

BOOKTYPE_MAX_USERS = 0
BOOKTYPE_MAX_BOOKS = 0

# These are default options for CSS settings

BOOKTYPE_CSS_BOOK = '.objavi-chapter{ \n  color: #000; \n} \n\na { \n  text-decoration:none; \n  color:#000; \n} \n\nh1 .initial{ \n  color: #000; \n} \n\n.objavi-subsection{ \n  display: block; \n  page-break-before: always; \n/* page-break-after: always;*/ \n  text-transform: uppercase; \n  font-size: 20pt; \n} \n\nbody .objavi-subsection:first-child{ \n  page-break-before: avoid; \n} \n\n\n.objavi-subsection .initial { \n  font-size: 1em; \n  color: #000; \n} \n\n.objavi-subsection-heading { \n  font-size: 20pt; \n  text-align: center; \n  line-height: 300px; \n  font-weight: normal; \n} \n\n\nh1 { \n  page-break-before: always; \n} \n\n\ntable { \n  float: none; \n} \n\nh1.frontpage{ \n  page-break-after:always; \n  margin-top:70%; \n  font-size: 20pt; \n  text-align: center; \n  page-break-before: avoid; \n  font-weight: normal; \n} \n\ndiv.copyright{ \n  padding: 1em; \n} \n/* TOC ******************************/ \ntable { \n  float: none; \n} \n\ntable.toc { \n  font-size: 1.1em; \n  width: 95%; \n} \n\ntable.toc td{ \n  vertical-align:top \n  padding-left: 0.5em; \n} \n\ntd.chapter { \n  padding: 0 0.5em; \n  text-align: right; \n} \n\ntable.toc td.pagenumber { \n  text-align: right; \n  vertical-align:bottom; \n} \n\ntd.section { \n  padding-top: 1.1em; \n  font-weight: bold; \n} \n/* End TOC **************************/ \n\n\npre { \n  overflow: hidden; \n  white-space: pre-wrap; \n} \n\n\nh1, h2, h3, h4, h5, h6{ \n  page-break-after: avoid; \n  page-break-inside: avoid; \n} \n\n\n.page-break{ \n  page-break-before: always; \n  height: 7em; \n  display: block; \n} \n\n\n#right-footer { \n  text-align: right; \n} \n\n#left-footer { \n  text-align: left; \n} \n\na { \n  word-wrap: break-word; \n} \n\n.objavi-no-page-break { \n  page-break-inside: avoid; \n} \n\n.unseen{ \n  z-index: -66; \n  margin-left: -1000pt; \n}\n\nsup {\n  vertical-align:text-top;\n  font-size:0.7em; \n}\n\nimg { max-width: 95%; }\n\np { word-wrap: break-word; }\n\nli { word-wrap: break-word; }\n \t '

BOOKTYPE_CSS_BOOKJS = '/* DOCUMENT */\n\n@page {\n    size: auto;\n}\n\n\nbody {\n    font-family: "Libertine Serif";\n    background-color: white;\n}\n\n\n/* CONTENT */\n\nimg {\n    max-width: 90%;\n    height: auto;\n    image-resolution: from-image;\n}\n\nsup  {\n    font-size: 80%;\n}\n\np {\n    line-height: 130%;\n    word-break: break-word;\n    /* text-align: justify; */\n    text-align: left;\n}\n\na {\n    color: #000;\n    text-decoration: none;\n    word-wrap: break-word;\n}\n\nol, ul {\n    text-align: justify;\n}\n\nli {\n    margin-left: 1em;\n    word-wrap: break-word;\n    page-break-inside: avoid;\n    windows: 4;\n    orphans: 4;\n}\n\n/* HEADINGS */\n\nh1 {\n\n}\n\nh1 .initial {\n    display: none;\n}\n\nh1 .subtitle {\n}\n\nh1 .author {\n    display: block;\n    margin-top: 0.2in;\n    font-weight: normal;\n}\n\nh1 .comma {\n    font-size: 22pt;\n    display: none;\n}\n\nh2 {\n    page-break-after: avoid;\n}\n\nh3 {\n    page-break-after: avoid;\n}\n\nh4 {\n    page-break-after: avoid;\n}\n\nh5 {\n    font-weight: normal;\n    text-align: left;\n    page-break-after: avoid;\n}\n\n/* CODE BLOCKS */\n\npre {\n    white-space: pre-wrap;       /* css-3 */\n    white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */\n    white-space: -pre-wrap;      /* Opera 4-6 */\n    white-space: -o-pre-wrap;    /* Opera 7 */\n    word-wrap: break-word;       /* Internet Explorer 5.5+ */\n    widows:4;\n    orphans:4;\n}\n\ncode {\n\n}\n\n\n\n/* TOC */\n\n#pagination-toc-title {\n    font-size: 20pt;\n    font-weight: 700;\n    text-align: left;\n    padding-bottom: .4in;\n}\n\n.pagination-toc-entry {\n/*    width: 6.2in; */\n    width: 90%;\n    display: block;\n    padding-bottom: .3in;\n    font-size: 16pt;\n}\n\n.pagination-toc-entry .pagination-toc-pagenumber {\n    font-weight: 400;\n    display: inline-block;\n    vertical-align: text-bottom;\n    font-size: 16pt;\n    float:right; /* SET AUTOMATICALLY */\n}\n\n.pagination-toc-entry.section {\n    font-weight:700;\n    font-size: 16pt;\n    text-transform: uppercase;\n    padding-bottom: .3in;\n}\n\n\n/* FRONT MATTER */\n\n#booktitle {\n    margin-top: 1.7in;\n    font-size: 26pt;\n    font-weight: normal;\n    text-align: center;\n    text-transform: uppercase;\n}\n\n#booksubtitle {\n    font-size: 22px;\n    margin-top: 0.2in;\n    font-weight: normal;\n    text-align: center;\n}\n\n#bookeditors {\n    padding-top: 1.5in;\n    font-weight: normal;\n    text-align: center;\n    font-size: 24pt;\n}\n\n#bookpress {\n    padding-top: 1.8in;\n    font-weight: normal;\n    text-align: center;\n    font-size: 24pt;\n}\n\n#copyrightpage {\n    font-weight: normal;\n    font-size: 18pt;\n    padding-top: 0.2in;\n}\n\n\n/* HEADER */\n\n.pagination-header {\n   font-size: 12pt;\n   font-weight: light;\n}\n\n.pagination-pagenumber {\n   font-size: 12pt;\n}\n\n.pagination-header .pagination-section { display: none; }\n\n\n.pagination-toc-text .initial { display: none; }\n.pagination-chapter .initial { display: none; }\n\n\n/* MISC */\n\n.imagecaption {\n    font-size: 9pt;\n    padding-left: 0.2in;\n    line-height: 18px;\n    text-align: justify;\n    font-weight: normal;\n    display: block;\n}\n\n\n.pagebreak {\n    -webkit-region-break-after: always;\n}\n\n.pagebreakbefore {\n    -webkit-region-break-before: always;\n}\n\n.objavi-chapter .initial {\n    display: none;\n}\n\n.objavi-subsection {\n    display: none;\n}\n\n.objavi-subsection-heading {\n    line-height: 120px !important;\n    /* work-around to make section title pages no longer than one page */\n    font-size: 22px;\n    font-weight: bold;\n    text-align: left;\n    display: none;\n}\n\n@media screen {\n    .page {\n        border: solid 1px #000;\n        margin-bottom: .2in;\n    }\n\n    body {\n	background-color: #efefef;\n    }\n}\n\n\n'

BOOKTYPE_CSS_EBOOK = '.objavi-chapter{\n  color: #000;\n  display:none;\n} \n\na {\n  text-decoration:none;\n  color:#000;\n} \n\nh1 .initial{\n  color: #000;\n  display:none;\n} \n\n.objavi-subsection{\n  display: block;\n  page-break-before: always;\n} \n\nbody .objavi-subsection:first-child{\n  page-break-before: avoid;\n} \n\n.objavi-subsection .initial {\n  color: #000;\n  display:none;\n} \n\n.objavi-subsection-heading {\n  font-size: 20pt;\n  text-align: center;\n  line-height: 300px;\n  font-weight: normal;\n} \n\ntable {\n  float: none;\n} \n\nh1.frontpage{\n  page-break-after:always;\n  margin-top:70%;\n  font-size: 20pt;\n  text-align: center;\n  page-break-before: avoid;\n  max-width: 700pt;\n  font-weight: normal;\n} \n\ndiv.copyright{\n  padding: 1em;\n}\n/* TOC ******************************/\ntable {\n  float: none;\n} \n\ntable.toc {\n  font-size: 1.1em;\n  width: 95%;\n} \n\ntable.toc td {\n  vertical-align:top\n  padding-left: 0.5em;\n} \n\ntd.chapter {\n  padding: 0 0.5em;\n  text-align: right;\n} \n\ntable.toc td.pagenumber {\n  text-align: right;\n  vertical-align:bottom;\n} \n\ntd.section {\n  padding-top: 1.1em;\n  font-weight: bold;\n}\n\t\t\t\t\t\n/* End TOC **************************/ \nimg {\n   max-width: 500px;\n   height: auto;\n} \n\n.objavi-no-page-break {\n   page-break-inside: avoid;\n} \n\n.unseen {\n   z-index: -66;\n   margin-left: -1000pt;\n} \n\n.objavi-subsection-heading{\n  height:860px;\n  font-size:0px;\n  display:block;\n}\n'

BOOKTYPE_CSS_PDF = '.objavi-subsection{ \n  display: block; \n  page-break-before: always; \n/* page-break-after: always;*/ \n  text-transform: uppercase; \n  font-size: 20pt; \n} \n\nbody .objavi-subsection:first-child{ \n  page-break-before: avoid; \n} \n\n\n.objavi-subsection .initial { \n  font-size: 1em; \n  color: #000; \n} \n\n.objavi-subsection-heading { \n  font-size: 20pt; \n  text-align: center; \n  line-height: 300px; \n  font-weight: normal; \n} \n\n\nh1 { \n  page-break-before: always; \n} \n\n\ntable { \n  float: none; \n} \n\nh1.frontpage{ \n  page-break-after:always; \n  margin-top:70%; \n  font-size: 20pt; \n  text-align: center; \n  page-break-before: avoid; \n  font-weight: normal; \n} \n\ndiv.copyright{ \n  padding: 1em; \n} \n/* TOC ******************************/ \ntable { \n  float: none; \n} \n\ntable.toc { \n  font-size: 1.1em; \n  width: 95%; \n} \n\ntable.toc td{ \n  vertical-align:top \n  padding-left: 0.5em; \n} \n\ntd.chapter { \n  padding: 0 0.5em; \n  text-align: right; \n} \n\ntable.toc td.pagenumber { \n  text-align: right; \n  vertical-align:bottom; \n} \n\ntd.section { \n  padding-top: 1.1em; \n  font-weight: bold; \n} \n/* End TOC **************************/ \n\n\n\npre { \n  overflow: hidden; \n  white-space: pre-wrap; \n} \n\n\nh1, h2, h3, h4, h5, h6{ \n  page-break-after: avoid; \n  page-break-inside: avoid; \n} \n\n\n.page-break{ \n  page-break-before: always; \n  height: 7em; \n  display: block; \n} \n\na { \n  word-wrap: break-word; \n} \n\n.objavi-no-page-break { \n  page-break-inside: avoid; \n} \n\n/*To force a blank page it is sometimes necessary to add unseen \n content. Display:none and visibility: hidden do not work -- the \n renderer realises that they are not there and skips the page. So we \n add a tiny bit of text beyond the margin of the page. \n*/ \n.unseen{ \n  z-index: -66; \n  margin-left: -1000pt; \n}\n\nimg { max-width: 95%; }\n\np { word-wrap: break-word; }\n\nli { word-wrap: break-word; }\n  '

BOOKTYPE_CSS_ODT = 'body {\n}\n\n#book-title {\n    font-size: 64pt;\n    page-break-before: avoid;\n    margin-bottom: 12em;  \n    max-width: 700px;\n}\n\n.unseen {\n    display: none;\n}\n\n.chapter {\n    color: #000;\n}\n\nh1 .initial {\n    color: #000;\n    font-size: 2em;\n}\n\nbody .subsection:first-child {\n}\n\nh1 {\n  page-break-before: always;\n}\n\n.objavi-subsection{\n   text-transform: uppercase;\n   font-size: 20pt;\n}\n\n.objavi-subsection .initial {\n   font-size: 1em;\n   color: #000;\n}\n\n.objavi-subsection-heading{\n   font-size: 36pt;\n   font-weight: bold;\n   page-break-before: always;\n}\n\ntable {\n   float: none;\n}\n\nh1.frontpage{\n   font-size: 64pt;\n   text-align: center;\n   max-width: 700px;\n}\n\ndiv.copyright{\n    padding: 1em;\n}\n\npre {\n   max-width:700px;\n   overflow: hidden;\n}\n\nimg {\n   max-width: 700px;\n   height: auto;\n}\n'
