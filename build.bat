del *.aux
del *.gz
del *.log
del *.out
del *.pdf
del *.toc
del *.vrb
del *.gz(busy)
del *.pyg
pdflatex -shell-escape -synctex=1 -interaction=nonstopmode "ProblemBook.NET".tex
pdflatex -shell-escape -synctex=1 -interaction=nonstopmode "ProblemBook.NET".tex