from lxml import etree
from smartypants import smartypants

parser = etree.XMLParser()

# Substitute the appropriate filename for the XML file you have.
tree = etree.parse('no-entities-ls.xml')
text = tree.xpath("//text()")
text = ''.join(text).split('\n')

for line in text:
    print(line)
    # Comment out the previous line and uncomment the next print statement for
    # curly quotes instead of straight quotes. NB: the process will take
    # significantly longer if you do this.
    # print(smartypants(line))
