# -*- coding: utf-8 -*-
## $Id$
##
## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""CDS Invenio international messages functions, to be used by all
I18N interfaces.  Typical usage in the caller code is:

   from messages import gettext_set_language
   [...]
   def square(x, ln=cdslang):
       _ = gettext_set_language(ln)
       print _("Hello there!")
       print _("The square of %s is %s.") % (x, x*x)

In the caller code, all output strings should be made translatable via
the _() convention.

For more information, see ABOUT-NLS file.
"""

__revision__ = "$Id$"

import gettext

from invenio.config import localedir, cdslangs

lang = {}
for ln in cdslangs:
    lang[ln] = gettext.translation('cds-invenio', localedir, languages = [ln], fallback = True)

def gettext_set_language(ln):
    """
      Set the _ gettext function in every caller function

      Usage::
        _ = gettext_set_language(ln)
    """
    return lang[ln].gettext

def wash_language(ln):
    """Look at LN and check if it is one of allowed languages for the interface.
       Return it in case of success, return the default language otherwise."""
    if ln in cdslangs:
        return ln
    else:
        return 'en'

def language_list_long():
    """Return list of [short name, long name] for all enabled languages."""
    cfg_all_language_names = {'bg': 'Български',
                              'ca': 'Català',
                              'cs': 'Česky',
                              'de': 'Deutsch',
                              'el': 'Ελληνικά',
                              'en': 'English',
                              'es': 'Español',
                              'fr': 'Français',
                              'hr': 'Hrvatski',
                              'it': 'Italiano',
                              'ja': '日本語',
                              'no': 'Norsk/Bokmål',
                              'pl': 'Polski',
                              'pt': 'Português',
                              'ru': 'Русский',
                              'sk': 'Slovensky',
                              'sv': 'Svenska',
                              'uk': 'Українська',
                              'zh_CN': '中文(简)',
                              'zh_TW': '中文(繁)',}
    enabled_lang_list = []
    for lang in cdslangs:
        enabled_lang_list.append([lang,cfg_all_language_names[lang]])
    return enabled_lang_list