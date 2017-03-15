run_test:
	make -C test test

run_clitests:
	make -C test clitests

README.html: README.md
	pandoc -f markdown -t html README.md >README.html

manpages:
	tools/build_manpages.py

doc:
	pandoc test.md test.md -s -t man >man/test.1
	pandoc test.md test.md -s -t html >test.html

clean:
	rm README.html
