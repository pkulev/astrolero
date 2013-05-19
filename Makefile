clean:
	rm -f *~ *.pyc \#*
count:
	printf "%d lines of python code\n  \t%d lines in hw.py\n \t%d lines in memorypazzle.py\n" `cat *.py| wc -l` `cat hw.py| wc -l` `cat memorypazzle.py| wc -l` 
run:
	python -tt memorypazzle.py

.PHONY: clean count run
