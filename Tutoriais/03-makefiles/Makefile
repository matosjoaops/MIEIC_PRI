.PHONY: alice.csv

output: alice.csv

alice.csv: alice.txt
	cat alice.txt | tr ' ' ',' > alice.csv

alice.txt:
	curl "https://www.gutenberg.org/files/11/11-0.txt" > alice.txt