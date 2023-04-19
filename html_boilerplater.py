#!/usr/bin/env python3

"""
A script to create HTML-files with some boilerplate content.

Useful when setting up routing to render HTML-files without having to complete all the
specific content for each file.

Use `-h` flag for more info on usage.
"""

import argparse
import os

CWD = os.getcwd()

# Parse CLI arguments.
parser = argparse.ArgumentParser()
# Jinja template.
parser.add_argument(
    "-j",
    "--jinja",
    nargs="?",
    const=True,
    help=(
        """
        Add Jinja template tags and a base html file that others extends from.
        The base document includes a header and a footer partial template.
        """
    ),
),
args = parser.parse_args()

# Welcome message.
print("Welcome to HTML Bare Template creator")
print(f"Files will be created in {CWD}\n")
if args.jinja:
    print("\nExtensions of a predefined base template will be created")
    print("The templates will contain a <h1> tag with the name of the file")
    print("The name of the project will be included int the page titles")
    print("The name of the app is used when referencing template inheritance\n")
else:
    print("A HTML file with a <h1> tag with the name of the file will be created")

# Split cwd path to find suggestions for project and app names.
paths = CWD.split("/")
# Suggested project name.
if args.jinja:
    # Based on the project/app/templates/app/ directory structure common in Django.
    project_suggestion = paths[-4]
    app_suggestion = paths[-1]
else:
    project_suggestion = paths[-1]

# Get name of project.
project_name = input(f"Project name: [{project_suggestion}]")
# Set given or suggested project name.
if len(project_name) == 0:
    # No lower() method to ensure paths are correct.
    project_name = project_suggestion
else:
    project_name = project_name.lower().strip()

# Get name of app.
if args.jinja:
    app_name = input(f"App name: [{app_suggestion}]").lower().strip()
    # Ensure an app name has been given.
    if len(app_name) == 0:
        # No lower() method to ensure paths are correct.
        app_name = app_suggestion
    else:
        app_name = app_name.lower().strip()

# Make list of files to create.
print("Enter the name(s) of the HTML files")
print("Enter 'q' when no more files are to be created")
filenames = []
while True:
    # Ensure no duplication of .html file extension.
    filename = input("Filename: ").removesuffix(".html")
    if filename.lower() == "q":
        break
    filenames.append(filename)
# Check if jinja template inheritance is to be used.
if args.jinja:
    # Add base-, header-, footer.html to list of files to create.
    jinja_files = ["base", "_header", "_footer"]
    filenames.extend(jinja_files)

# Remove possible duplicate filenames.
filenames = set(filenames)
for filename in filenames:
    # Set content for jinja templates.
    if args.jinja:
        if filename == "base":
            content = f"""<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{% block title %}}{{% endblock %}} | {project_name}</title>
</head>

<body>
{{% include "{app_name}/_header.html" %}}

<main>
    {{% block content %}}{{% endblock %}}
</main>

{{% include "{app_name}/_footer.html" %}}
</body>

</html>
"""
        elif filename == "_header":
            content = f"""<header>
    <h1>{project_name}</h1>
    <nav>

    </nav>
</header>
"""
        elif filename == "_footer":
            content = f"""<footer>

</footer>
"""
        else:
            # Write name of file in html-document.
            content = f"""{{% extends "{app_name}/base.html" %}}

{{% block title %}}{filename}{{% endblock %}}

{{% block content %}}
<h1>{filename}</h1>

{{% endblock %}}
"""
    # Set content for vanilla HTML-files.
    else:
        content = f"<h1>{filename}</h1>"

    with open(f"{filename}.html", "w") as f:
        f.write(content)
