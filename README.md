# first-edit
first-edit lets writers know if they are repeating words -- something that they hate doing.

# Background
Editing long documents is a pain. One of the things I check for while reviewing my online drafts is whether I'm using a particular word too many times. This task ought to be trivial but is actually far from it. I copy-paste the content to Word, and then manually use CTRL-F to find words that I think I might have repeated. This process is not only tedious, but also has the risk of me missing out on some duplicate words that I didn't think of.

first-edit is therefore a quick way for writers to find out if they're using any words too often.

# Usage
- Have Python installed on your computer.
- Copy-Paste first_edit.py to the folder that contains the document you want to analyze.
- Run first_edit.py. When prompted, type the name of the document you want to analyze. <i>first-edit currently only works with <b>.txt</b> files.</i>
- See the analysis of your content in analysis_file.txt.
- If the analysis contains some common words that you want to ignore, you can explicitly specify these words in ignore_words.csv.
