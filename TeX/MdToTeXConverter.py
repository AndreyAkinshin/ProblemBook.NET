# -*- coding: utf-8 -*-
import mistune
import sys
import re
from os import listdir
from os.path import isfile, join

reload(sys)
sys.setdefaultencoding('utf-8')

BEGIN = r'\begin{%s}'
END = r'\end{%s}'
enclose = lambda t, s: '\n%s\n%s\n%s\n' % (BEGIN % (t, ), s, END % (t, ))

def LaTeXEscape(str):
    return str.replace("#", r"\#").replace("-&gt;", r"--->").replace("&gt;", ">").replace("&lt;", "<")

class LaTeXRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        return enclose('source', code)

    def codespan(self, text):
        return r'\code{%s}' % (text, )

    def block_quote(self, text):
        return enclose('quotation', text)

    def header(self, text, level, raw=None):
        return '\\' + 'sub' * (level - 1) + 'section' + '{%s}\n' % (text)

    def list(self, body, ordered=True):
        return enclose('itemize', body)
        pass

    def list_item(self, text):
        return r'\item ' + LaTeXEscape(text) + '\n'

    def paragraph(self, text):
        return LaTeXEscape(text) + '\n\n'

    def linebreak(self):
        return '\n'

    def emphasis(self, text):
        return r'\textit{%s}' % (text, )

    def double_emphasis(self, text):
        return r'\textbf{%s}' % (text, )

    def hrule(self):
        return r'\hrulefill'

    def footnotes(self, text):
        print(text)
        return text

    def footnote_ref(self, key, index):
        print(key, index)
        return r'\footnotemark[%s]' % (key, )

    def footnote_item(self, key, text):
        return r'\footnotetext[%s]{%s}' % (key, text)

    def reference(self, key):
        return r'\cite{%s}' % (key, )

    def link(self, link, title, content):
        return r'\href{%s}{%s}' % (link, content)

    def image(self, src, title, text):
        return '\n'.join([r'\begin{figure}', 
                          r'\includegraphics{%s}' % (src, ), 
                          r'\caption{%s}' % (title, ), 
                          r'\label{%s}' % (text, ), 
                          r'\end{figure}'])

renderer = LaTeXRenderer()
md = mistune.Markdown(renderer=renderer)

def renderFile(filename, isProblem = False):
    with open(filename) as f:
        content = f.readlines()
    if isProblem:
        content = content[1:len(content)-2]
    if isProblem:
        for x in xrange(1, len(content)):
            if (content[x].startswith("##")):
                content[x] = r"\textbf{" + content[x][2:].strip() + r"}" + "\n"
    content = "".join(content)
    return md.render(content)

def convert(locale):
    rootDir = "../%s/" % (locale,)
    if locale is "ru":
        literalProblem = "Задача"
        literalSolution = "Решение"
        literalLeftQuote = "<<"
        literalRightQuote = ">>"
    if locale is "en":
        literalProblem = "Problem"
        literalSolution = "Solution"
        literalLeftQuote = "``"
        literalRightQuote = "''"
    tex = ""
    with open(join(rootDir, "SUMMARY.md")) as f:
        summary = f.readlines()
    enumerateMode = False
    summaryRegex = r"\[(.+)\]\((.+)\)"
    for summaryLine in summary:
        links = re.findall(summaryRegex, summaryLine)
        if summaryLine.startswith("<!--"):
            if enumerateMode is True:
                enumerateMode = False
                tex += r"\end{enumerate}" + "\n"
            title = summaryLine[4:-4]
            text = r"\chapter*{%s}\addcontentsline{toc}{chapter}{%s}" % (title,title)
            tex += text + "\n"
        elif (len(links) > 0):
            title = links[0][0]
            link = links[0][1]
            if not summaryLine.startswith(" "):
                if enumerateMode is True:
                    enumerateMode = False
                    tex += r"\end{enumerate}" + "\n"
                renderedFile = renderFile(join(rootDir, link))
                if "INTRODUCTION.md" in link:
                    renderedFile = re.compile(r"\\section\{(.+)\}").sub(r"\\chapter*{\1}\\addcontentsline{toc}{chapter}{\1}", renderedFile).replace(r"\subsection", r"\section*")
                else:
                    renderedFile = r"\section{%s}" % title
                tex += renderedFile + "\n"
            elif summaryLine.startswith(" "):
                if enumerateMode is False:
                    enumerateMode = True
                    tex += r"\begin{enumerate}" + "\n"
                renderedFile = renderFile(join(rootDir, link), True)
                label = link.replace("/", ":").replace("-P", "").replace("-S", "").replace(".md", "")
                if "-P.md" in link:
                    tex += "\n".join([
                        r"",
                        r"\begin{samepage}",
                        r"\item \label{problem:%s}" % (label, ),
                        renderedFile,
                        r"\nopagebreak \par \nopagebreak",
                        r"\internalhref{solution:%s}{%s}" % (label, literalSolution),
                        r"\end{samepage}"]) + "\n"
                if "-S.md" in link:
                    tex += "\n".join([
                        r"",
                        #r"\begin{samepage}",
                        r"\item \label{solution:%s}" % (label, ),
                        r"\internalhref{problem:%s}{%s %s%s%s}" % (label, literalProblem, literalLeftQuote, label, literalRightQuote),
                        r"\nopagebreak \par \nopagebreak",
                        renderedFile,
                        #r"\end{samepage}"],
                        ""]) + "\n"

    if enumerateMode is True:
        enumerateMode = False
        tex += r"\end{enumerate}" + "\n"

    with open("content-%s.tex" % (locale,), 'w') as f:
        f.write(tex)

convert("ru")
convert("en")