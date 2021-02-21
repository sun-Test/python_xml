'''

'''

from lxml import etree

class XmlUtils():

    def __init__(self) -> None:
        pass

    @staticmethod
    def firstXpathObject(ele, xpathExpression, nameSpaces):
        res = etree.XPath(xpathExpression, namespaces = nameSpaces)(ele)
        return res[0] if len(res) > 0 else None

class XmlSearch():
    
    def __init__(self, xmlFile, nameSpaces) -> None:
        self.doc = etree.parse(xmlFile)
        self.root = self.doc.getroot()
        self.nameSpaces = nameSpaces

def testFunc01(xmlSearch):
    namePath = './/ns:name/text()'
    print(XmlUtils.firstXpathObject(xmlSearch.root, namePath, xmlSearch.nameSpaces))

def testFindLombokDependency(xmlSearch):
    lombokPath = './/ns:dependency/ns:groupId[text()=$grpId]'
    groupId = etree.XPath(lombokPath, namespaces= xmlSearch.nameSpaces)(xmlSearch.root, grpId = 'org.projectlombok')
    if len(groupId ) > 0:
        children = groupId[0].getparent().getchildren()
        for i in children:
            print(i.text)

def testFindLombokDependencyWithAnd(xmlSearch):
    '''
    test finding element with xpath and operator and
    '''
    lombokPath = './/ns:dependency/ns:groupId[text()=$grpId and @prop01=$prop]'
    groupId = etree.XPath(lombokPath, namespaces= xmlSearch.nameSpaces)(xmlSearch.root, grpId = 'org.projectlombok', prop='orange')
    if len(groupId ) > 0:
        children = groupId[0].getparent().getchildren()
        for i in children:
            print(i.text)



if __name__ == '__main__':
    search = XmlSearch('pom.xml', {'ns': "http://maven.apache.org/POM/4.0.0"})
    testFunc01(search)
    testFindLombokDependency(search)
    testFindLombokDependencyWithAnd(search)