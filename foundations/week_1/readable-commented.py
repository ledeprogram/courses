#
# An example of well-commented, easily-readable Python code
#

import glob
import json

print '## Stats'
print ''

# Find all of the IPython Notebook files
python_filenames = glob.glob('*.ipynb')

# Loop through each file
for filename in python_filenames:
    # Initialize beginning line counts
    code_line_total = 0
    markdown_line_total = 0
    comment_line_total = 0

    # Print the file's name
    print "---- %s ----" % filename

    # Open up the file and grab the insides
    ipython_file = open(filename, 'rb')

    # Parse it into something Python can read using JSON
    # http://ipython.org/ipython-doc/rel-1.1.0/interactive/nbconvert.html#notebook-format
    # http://stackoverflow.com/questions/11126902/decoding-json-string-in-python
    notebook = json.loads(ipython_file.read())
    
    # A notebook is made out of worksheets, loop through each with 'for'
    # http://www.diveintopython.net/file_handling/for_loops.html
    for worksheet in notebook['worksheets']:
        
        # A worksheet is made out of cells, loop through each
        for cell in worksheet['cells']:
            
            # There are two types of cells - code and markdown
            if cell['cell_type'] == 'code':
                # The code is is stored in 'input'
                lines = cell['input']     
                
                # Get rid of the whitespace before/after lines
                # http://stackoverflow.com/questions/761804/trimming-a-string-in-python
                stripped_lines = [line.strip() for line in lines]

                # Don't count blank lines
                code_lines = [line for line in stripped_lines if line != '']

                # Separated out comment lines - they have a '#' in front
                comment_lines = [line for line in code_lines if line.startswith('#')]
                
                # Subtract the number of comment lines from the 
                # number of code lines for the final count
                code_line_count = len(code_lines) - len(comment_lines)

                # Add what we've found to the running totals
                code_line_total = code_line_total + code_line_count                
                comment_line_total = comment_line_total + len(comment_lines)
                
            elif cell['cell_type'] == 'markdown':
                # The markdown is stored in 'source'
                lines = cell['source']

                # Get rid of the whitespace before/after lines
                # http://stackoverflow.com/questions/761804/trimming-a-string-in-python
                stripped_lines = [line.strip() for line in lines]

                # Don't count blank lines
                markdown_lines = [line for line in stripped_lines if line != '']

                # Add what we've found to the running totals
                markdown_line_total = markdown_line_total + len(markdown_lines)

    # Print what we've found
    # http://stackoverflow.com/questions/14041791/print-variable-and-a-string-in-python
    print "Markdown: %s lines" % markdown_line_total
    print "Python: %s lines" % code_line_total
    print "Comments: %s lines" % comment_line_total
    print ''