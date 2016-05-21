from xml.dom import minidom
import os

def getAnnotations(fileUrl):

    xmldoc = minidom.parse(fileUrl)
    annotations = xmldoc.getElementsByTagName('annotation')
    resultList = []

    for annotation in annotations:
        date = annotation.getElementsByTagName('dc:date')[0]
        texts = annotation.getElementsByTagName('text')
        for asdf in texts:
            resultList.append([date.childNodes[0].nodeValue, asdf.childNodes[0].nodeValue])

    return resultList


def main():
    for file in os.listdir():
        if file.endswith('epub.annot'):
            bookName = file[0:file.find('.epub.annot')]
            fo = open(bookName + '.txt', 'w')
            annotations = getAnnotations(file)
            for annotation in annotations:
                fo.write('\t* ' + annotation[1] + '\n\n')

            print('Annotations of \'' + bookName + '\' is extracted to \'' + bookName + '.txt\' file')
            fo.close()

if __name__ == '__main__':
    main()