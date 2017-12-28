import nltk
from nltk.corpus import wordnet as wn

from nltk.stem.wordnet import WordNetLemmatizer

def checkWords(word):
    allText = []
    a = []
    v = []
    n = []

    with open("secondTask.html", "w+") as f:
        f.write("<html>"+"\n")
        f.write("<head></head>"+"\n")
        f.write("<body>"+"\n")
        f.write("<p>Nouns color is <span style='color:blue;'>blue</span><br>Adjectives color is <span style='color:red;'>red</span><br>Verbs color is <span style='color:green;'>green</span></p>")

        text = nltk.word_tokenize(word)
        for i in range(0, len(text)):
            w = nltk.pos_tag(text)[i]
            if "NN" in w:
                #f.write("<div style='color:blue;'>"+w[0]+"</div>")
                allText.append("<span style='color:blue;'>" + w[0] + " " + "</span>")
                n.append(w[0])
            elif "VB" in w:
                allText.append("<span style='color:green;'>" + w[0] + " " + "</span>")
                v.append(w[0])
            elif "JJ" in w:
                allText.append("<span style='color:red;'>" + w[0] + " " + "</span>")
                a.append(w[0])
            else:
                allText.append(text[i]+" ")
        f.write("<p>")
        for t in allText:
            f.writelines(str(t))
            if "." in t:
                f.write("<br>")
        f.write("</p>")

        verb_list = []
        adjective_list = []
        noun_list = []
        for word in range(0, len(v)):
            verb_list.append(WordNetLemmatizer().lemmatize(v[word]))
        for word in range(0, len(a)):
            adjective_list.append(WordNetLemmatizer().lemmatize(a[word]))
        for word in range(0, len(n)):
            noun_list.append(WordNetLemmatizer().lemmatize(n[word]))

        for i in set(verb_list):
            syn = wn.synsets(i)
            for j in range(0,len(syn)):
                syno = syn[j].lemmas()[0].name()
                if syno in set(verb_list) and i != syno:
                    if i not in set(verb_list):
                        continue
                    verb_list.remove(i)
                    print(i + " " + syno)

        for i in set(adjective_list):
            syn = wn.synsets(i)
            for j in range(0,len(syn)):
                syno = syn[j].lemmas()[0].name()
                if syno in set(adjective_list) and i != syno:
                    if i not in set(adjective_list):
                        continue
                    adjective_list.remove(i)
                    print(i + " " + syno)

        for i in set(noun_list):
            syn = wn.synsets(i)
            for j in range(0,len(syn)):
                syno = syn[j].lemmas()[0].name()
                if syno in set(noun_list) and i != syno:
                    if i not in set(noun_list):
                        continue
                    noun_list.remove(i)
                    print(i + " " + syno)

        f.write("<p>")

        f.write("Verbs(Operations, attributes or relationships): ")
        f.write("<br>")
        f.write(str(set(verb_list)) + " ")
        f.write("<br>")

        f.write("Adjective(Attributes candidates): ")
        f.write("<br>")
        f.write(str(set(adjective_list)) + " ")
        f.write("<br>")

        f.write("Noun(Candidate classes): ")
        f.write("<br>")
        f.write(str(set(noun_list)) + " ")
        f.write("<br>")

        f.write("</p>")
        f.write("</body>"+"\n")
        f.write("</html>")
        f.close()

with open("grammarInputFile2.txt","r") as f:
    input = f.read()
f.close()


checkWords(input)
