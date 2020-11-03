.PHONY: default # Build the Tor exit node database
.PHONY: push # Push to all remote servers

default:
	@./tor.py

push:
	@git push origin --all
	@git push devforce --all