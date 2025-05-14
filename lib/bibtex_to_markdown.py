import bibtexparser
import os

bibtex_file="/home/karu/personalweb/themes/personal/static/test.bib"
markdown_folder="/home/karu/personalweb/content/ref/"
library = bibtexparser.parse_file(bibtex_file)
entries = library.entries

for e in entries:
    content = '---\n'
    file = markdown_folder+e.key+".md"
    for f in e.fields:
        content += f.key+': "'+f.value+'"\n'
        print(f.key)
    print(content)
    if e.entry_type == 'book':
        content += 'ref_type: "book"\n'
    else:
        content += 'ref_type: "article"\n'

    content += 'type: reference\n'
    content += '---'

    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write(content)

