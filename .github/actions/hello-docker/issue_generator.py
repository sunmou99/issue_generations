import json
import sys

if len(sys.argv) < 2:
    print('Missing arg json')
    sys.exit(1)

input = sys.argv[1]
issue = json.loads(input)
issue_title = issue['title']
issue_description = issue.get('description', 'Failures are detected in workflow(s):')
issue_tag = issue['issue_tag']
attached_to_last_issue = issue['attached_to_last_issue']
test_results = issue['test_results']


text = []
text.append('# ' + issue_title)
text.append(issue_description)

separator = ' | '
divider = '------------'
for result in test_results:
    table_name = result['table_name']
    text.append('## ' + table_name)
    colunms = result['colunm_names']
    text.append(separator.join(colunms))
    text.append(separator.join([divider for i in range(len(colunms))]))
    contents = result['contents']
    for content in contents:
        row = ['']
        for colunm in colunms:
            row.append(content.get(colunm, ''))
        row.append('')
    text.append(separator.join(row))

print('\n'.join(text))
