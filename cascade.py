'''
#Cascade
This pelican plugin adds css classes to nonstatic html output.

This is especially useful if you need to add attributes to a markdown item that 
are not easily modified using the python Attribute Lists markdown extension.

Consider using [Attribute Lists](https://python-markdown.github.io/extensions/attr_list/)
whenever possible. 
'''

import logging

try:
    from bs4 import BeautifulSoup
except ImportError:
    logger.error('BeautifulSoup not found')


from pelican import contents, signals
from pelican.settings import DEFAULT_CONFIG

logger = logging.getLogger(__name__)


def initialized(pelican):

    DEFAULT_CONFIG.setdefault('CASCADE_CSS', {})

    if pelican:
        pelican.settings.setdefault('CASCADE_CSS', {})


def replace_in_with(searchterm, soup, attributes):
    logger.debug('CASCADE Search Term: {0}; Count: {1}'.format(
        searchterm, len(soup.select(searchterm))))
    for item in soup.select(searchterm):

        attribute_set = set(item.attrs.get('class', []) + attributes)
        item.attrs['class'] = list(attribute_set)


def cascade(content):
    if isinstance(content, contents.Static):
        return

    replacements = content.settings['CASCADE_CSS']
    soup = BeautifulSoup(content._content, 'html.parser')

    for selector, classes in replacements.items():
        replace_in_with(selector, soup, classes)

    content._content = soup.decode()


def register():
    signals.initialized.connect(initialized)
    signals.content_object_init.connect(cascade)
