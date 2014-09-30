del *.aux
del *.gz
del *.log
del *.out
del *.pdf
del *.toc
del *.vrb
del *.gz(busy)
del *.pyg
python MdToTeXConverter.py
pdflatex -shell-escape -synctex=1 -interaction=nonstopmode "ProblemBook.NET-ru".tex
pdflatex -shell-escape -synctex=1 -interaction=nonstopmode "ProblemBook.NET-ru".tex
pdflatex -shell-escape -synctex=1 -interaction=nonstopmode "ProblemBook.NET-en".tex
pdflatex -shell-escape -synctex=1 -interaction=nonstopmode "ProblemBook.NET-en".tex