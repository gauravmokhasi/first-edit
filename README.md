# first-edit
first-edit lets writers know if they are repeating words -- something that they hate doing.

# Background
Editing long documents is a pain. One of the things I check for while reviewing my online drafts is whether I'm using a particular word too many times. I manually use CTRL-F to find words that I think I might have repeated. This process has the risk of me missing out on some duplicate words just because I didn't think of them.

first-edit is therefore a quick way for writers like me to find out if they're using any words too often.

# Usage
- Have Python installed on your computer.
- Download this repository to your computer, and unzip to a location of your choice.
- Copy-Paste the text document you want to analyze to the location where you unzipped the repository, i.e. the folder containing `first_edit_py2.py`, `first_edit_py3.py` and `ignore_words.csv`.
- Depending on the version of Python you have (2 or 3), run the appropriate `first_edit` file. When prompted, type the name of the document you want to analyze.
  - first-edit currently only works with <b>.txt</b> files.
- See the analysis of your content in `analysis_file.txt`.
- If the analysis contains some common words that you want to ignore, you can explicitly specify these words in `ignore_words.csv`. Subsequent runs of first edit will not count these words.
