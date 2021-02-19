import pathlib

here = pathlib.Path(__file__).parent
file_readme = here / '../../test.md'
with open(file_readme, 'r') as read_readme:
    content_readme = read_readme.readlines()


def content_about():
    """
    Looks for trailing slashes and words separated by commas at
    every "Content about:" section found in the readme.md file
    (this is, the list itself).

    result (str): return value of the function.
    checker (str): detector of the line corresponding the file.
    """

    result = 'No errors found.'
    checker = 'Content about:'

    for line, value in enumerate(content_readme):
        if checker in value:
            # words = i[len(checker):-2].split(', ')
            # Check for trailing slash
            if value[-1] != '\\':
                last = value[-2:-1]
                replaced = last.replace(' ', '\\', 1)
                content_readme[line] = value[:-2] + ' ' + replaced + '\n'
                with open(file_readme, 'w') as write_readme:
                    write_readme.writelines(content_readme)
                result = "Found errors. Fixed them."
            # Check for comma separated words

    return result


print(content_about())
