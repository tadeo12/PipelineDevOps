"""
This module create a 'build' directory if it doesn't exist 
and write a simple "index.html" file in it
"""

import os

# Create a 'build' directory if it doesn't exist
if not os.path.exists('build'):
    os.makedirs('build')

# Define the content of the HTML file
HTML_CONTENT= '''
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to my website!</h1>
    <p>Thanks for visiting.</p>
</body>
</html>
'''

# Write the content to the index.html file in the 'build' directory
with open('build/index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print('index.html file created in build directory.')