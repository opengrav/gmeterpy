# Makefile for Sphinx documentation
#

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXAUTOGEN = sphinx-autogen
SOURCEDIR     = .
BUILDDIR      = _build

.PHONY: help clean api html linkcheck doctest serve

all: html

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	rm -rf $(BUILDDIR)/* $(SOURCEDIR)/api/_autosummary

api:
	@echo
	@echo "Building API Reference."
	@echo
	@$(SPHINXAUTOGEN) -i -t $(SOURCEDIR)/_templates -o $(SOURCEDIR)/api/_autosummary $(SOURCEDIR)/api/*.rst

html: api
	@echo
	@echo "Building HTML files."
	@echo
	$(SPHINXBUILD) -b html -d $(BUILDDIR)/doctrees $(SPHINXOPTS) . $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

linkcheck: api
	$(SPHINXBUILD) -b linkcheck -d $(BUILDDIR)/doctrees $(SPHINXOPTS) . $(BUILDDIR)/linkcheck

doctest: api
	$(SPHINXBUILD) -b doctest -d $(BUILDDIR)/doctrees $(SPHINXOPTS) . $(BUILDDIR)/doctest

serve:
	cd $(BUILDDIR)/html && python -m http.server 8001
