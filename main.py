"""
This module creates a 'build' directory if it doesn't exist
and writes a simple "index.html" file in it.
"""

import os


def create_index_html():
    """
    This function creates a 'build' directory if it doesn't exist
    and writes a simple "index.html" file in it.
    """
    # Create a 'build' directory if it doesn't exist
    if not os.path.exists('build'):
        os.makedirs('build')

    # Define the content of the HTML file
    html_content = '''
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
    with open('build/index.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    print('index.html file created in build directory.')


def main():
    """
    Calls the create_index_html() function to create an index.html file
    in the 'build' directory.
    """
    create_index_html()


if __name__ == '__main__':
    """
    Runs the main function if this module is run as the main program.
    """
    main()
