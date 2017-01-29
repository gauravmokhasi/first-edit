# first-edit
first-edit lets writers know if they are repeating words -- something that they hate doing.

# Background
Editing long documents is a pain. One of the things I check for while reviewing my online drafts is whether I'm using a particular order too many times. This task ought to be trivial but is actually far from it. I usually copy-paste the content to Word, and then manually use CTRL-F for words that I think I might have repeated. This process is not only tedious, but also has the risk of me missing out on duplicate words that I might not have thought of.

first-edit is therefore a quick way for writers to find out if they're using particular words too often.

# Usage
- Have Python installed in your computer.
- Copy-Paste first_edit.py to the folder that contains the document you want to analyze.
- Run first_edit.py. Type the name of the document you want to analyze when prompted. <i>first-edit currently only works with <b>.txt</b> files.</i>
- See the analysis in analysis_file.txt.
- If the analysis contains somey common words that you want to ignore, you can explicitly specify these words in ignore_words.csv.
