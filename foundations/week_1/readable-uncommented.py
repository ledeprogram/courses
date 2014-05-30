#
# An example of uncommented, easily-readable Python code
#

import glob
import json

print '## Stats'
print ''

python_filenames = glob.glob('*.ipynb')

for filename in python_filenames:
    code_line_total = 0
    markdown_line_total = 0
    comment_line_total = 0

    ipython_file = open(filename, 'rb')
    notebook = json.loads(ipython_file.read())

    for worksheet in notebook['worksheets']:
        for cell in worksheet['cells']:
            if cell['cell_type'] == 'code':
                lines = cell['input']     
                stripped_lines = [line.strip() for line in lines]
                code_lines = [line for line in stripped_lines if line != '']
                comment_lines = [line for line in code_lines if line.startswith('#')]
                code_line_count = len(code_lines) - len(comment_lines)
                code_line_total = code_line_total + code_line_count                
                comment_line_total = comment_line_total + len(comment_lines)
            elif cell['cell_type'] == 'markdown':
                lines = cell['source']
                stripped_lines = [line.strip() for line in lines]
                markdown_lines = [line for line in stripped_lines if line != '']
                markdown_line_total = markdown_line_total + len(markdown_lines)

    print "---- %s ----" % filename
    print "Markdown: %s lines" % markdown_line_total
    print "Python: %s lines" % code_line_total
    print "Comments: %s lines" % comment_line_total
    print ''