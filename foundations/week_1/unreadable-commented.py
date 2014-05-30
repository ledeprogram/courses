#
# An example of well-commented, unreadable Python code
#

import glob
import json

print '## Stats'
print ''

# Loop through each file
for f in glob.glob('*.ipynb'):
    # Initialize comment line count, markdown line count and code line count
    cmt = 0
    mdt = 0
    cdt = 0

    # Open up the file and grab the insides
    ip = open(filename, 'rb')

    # Parse it into something Python can read using JSON
    # http://ipython.org/ipython-doc/rel-1.1.0/interactive/nbconvert.html#notebook-format
    # http://stackoverflow.com/questions/11126902/decoding-json-string-in-python
    nb = json.loads(ip.read())
    
    # A notebook is made out of worksheets, loop through each with 'for'
    # http://www.diveintopython.net/file_handling/for_loops.html
    for w in nb['worksheets']:
        
        # A worksheet is made out of cells, loop through each
        for c in w['cells']:
            
            # There are two types of cells - code and markdown
            if c['cell_type'] == 'code':
                # The code is is stored in 'input'
                x = c['input']     
                
                # Get rid of the whitespace before/after lines
                # http://stackoverflow.com/questions/761804/trimming-a-string-in-python
                y = [l.strip() for l in x]

                # Don't count blank lines
                cdl = [l for l in y if l != '']

                # Separated out comment lines - they have a '#' in front
                cml = [l for l in cdl if l.startswith('#')]
                
                # Subtract the number of comment lines from the 
                # number of code lines for the final code line count
                # Add what we've found to the running totals
                cdt = cdt + len(cdl) - len(cml)                
                cmt = cmt + len(cml)
                
            elif c['cell_type'] == 'markdown':
                # The markdown is stored in 'source'
                x = c['source']

                # Get rid of the whitespace before/after lines
                # http://stackoverflow.com/questions/761804/trimming-a-string-in-python
                y = [l.strip() for l in x]

                # Don't count blank lines
                mdl = [l for l in y if l != '']

                # Add what we've found to the running totals
                mdt = mdt + len(mdl)

    # Print the file's name
    print "---- %s ----" % f
    
    # Print what we've found
    # http://stackoverflow.com/questions/14041791/print-variable-and-a-string-in-python
    print "Markdown: %s lines" % mdt
    print "Python: %s lines" % cdt
    print "Comments: %s lines" % cmt
    print ''