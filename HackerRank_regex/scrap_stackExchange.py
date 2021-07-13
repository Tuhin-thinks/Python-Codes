import re, sys

stack = sys.stdin.read()

results = re.findall(r'question-summary-(\w\w\w\w\w)".*?class="question-hyperlink">(.+?)</a>.*?class=\"relativetime\">(.+?)</span>', stack, re.DOTALL)

for result in results:
	print(';'.join(result))