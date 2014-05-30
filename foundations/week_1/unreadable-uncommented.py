#
# An example of uncommented, unreadable Python code
#

import glob
import json

print '## Stats'
print ''

for f in glob.glob('*.ipynb'):
    cmt = 0
    mdt = 0
    cdt = 0
    ip = open(f, 'rb')
    nb = json.loads(ip.read())
    for w in nb['worksheets']:
        for c in w['cells']:
            if c['cell_type'] == 'code':
                x = c['input']     
                y = [l.strip() for l in x]
                cdl = [l for l in y if l != '']
                cml = [l for l in cdl if l.startswith('#')]
                cdt = cdt + len(cdl) - len(cml)                
                cmt = cmt + len(cml)
            elif c['cell_type'] == 'markdown':
                x = c['source']
                y = [l.strip() for l in x]
                mdl = [l for l in y if l != '']
                mdt = mdt + len(mdl)

    print "---- %s ----" % f
    print "Markdown: %s lines" % mdt
    print "Python: %s lines" % cdt
    print "Comments: %s lines" % cmt
    print ''