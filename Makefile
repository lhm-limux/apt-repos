run_test:
	make -C test test

run_clitests:
	make -C test clitests

README.html: README.md
	pandoc -f markdown -t html README.md >README.html

docs:
	mkdir -p doc/generated/man doc/generated/html
	for i in apt-repos apt-repos-ls apt-repos-show apt-repos-suites; do \
		tools/add_parser_infos_to_markdown_files.py doc/$$i.md; \
		pandoc doc/$$i.md -s -t man >doc/generated/man/$$i.1; \
		pandoc doc/$$i.md -s -t html >doc/generated/html/$$i.html; \
	done

clean:
	rm README.html
