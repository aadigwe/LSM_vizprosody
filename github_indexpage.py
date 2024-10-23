import os

def create_index_html(source_folder, index_file_path):
  """Creates an index HTML file with hyperlinks to nested HTML files.

  Args:
    source_folder: The path to the source folder containing the HTML files.
    index_file_path: The path of the index HTML file to create.
  """

  html_files = []
  for root, dirs, files in os.walk(source_folder):
    for file in files:
      if file.endswith(".html"):
        html_files.append(os.path.join(root, file))

  with open(index_file_path, "w") as index_file:
    index_file.write("<html>\n<body>\n")
    for html_file in html_files:
      relative_path = os.path.relpath(html_file, source_folder)
      index_file.write(f'<a href="{relative_path}">{relative_path}</a><br>\n')
    index_file.write("</body>\n</html>\n")

# Example usage:
source_folder = "/mnt/ceph_rbd/ICASSP24/DIVERSITY/stopes/LSM_vizprosody"
index_file_path = "index.html"

create_index_html(source_folder, index_file_path)