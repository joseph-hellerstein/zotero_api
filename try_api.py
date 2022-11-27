from pyzotero import zotero
library_id = 1083289
api_key = "7XgrdbyqabN6YkqV7Sw4X6CW"
library_type = "user"
zot = zotero.Zotero(library_id, library_type, api_key)
items = zot.top(limit=5)
# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
for item in items:
    print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))
for key, value in items[0]['data'].items():
    print("%s:  %s" % (str(key), str(value)))
