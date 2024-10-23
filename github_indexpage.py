import os
import datetime


def create_index_html(source_folder, index_file_path, title="Index of Exp Files"):
  """Creates an index HTML file with hyperlinks to nested HTML files.

  Args:
    source_folder: The path to the source folder containing the HTML files.
    index_file_path: The path of the index HTML file to create.
    title: The title of the index HTML page.
  """


  html_files = []
  todaydate = datetime.date.today()
  for root, dirs, files in os.walk(source_folder):
    for file in files:
      if file.endswith(".html"):
        html_files.append(os.path.join(root, file))

  with open(index_file_path, "w") as index_file:
    index_file.write(f"""<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
<style>
body {{
  font-family: Arial, sans-serif;
  margin: 20px;
}}

h1 {{
  text-align: center;
}}

ul {{
  list-style: none;
  padding: 0;
}}

li {{
  margin-bottom: 10px;
}}

a {{
  text-decoration: none;
  color: #007bff;
}}
</style>
</head>
<body>
<h1>{title}</h1>
<h3>Exploring Large Speech Models</h3>
<h3>Last updated: {todaydate}</h3>
<ul>
""")
    for html_file in html_files:
      relative_path = os.path.relpath(html_file, source_folder)
      index_file.write(f'<li><a href="{relative_path}">{relative_path}</a></li>\n')
    index_file.write("</ul>\n</body>\n</html>\n")

# Example usage:
source_folder = "/mnt/ceph_rbd/ICASSP24/DIVERSITY/stopes/LSM_vizprosody"
index_file_path = "index.html"

create_index_html(source_folder, index_file_path)

