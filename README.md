# KCEO Glossary

## Contributions and Feedback
The KCEO Glossary is built for the EO community. Your feedback and ideas are fundamental for the further development of this glossary. PR's and contributions of any kind are highly welcomed. 

### Contribution Guide
coming soon

## To Do's:
- Update GitHub actions to run custom scripts for cross linking, topology and dependency graph every time. Requires some careful testing. High priority.
- Add contribution guide in this readme. High priority.
- Update landing page search with new terms if found. Requires small Python script. Low priority for now.
- Add versioning with mike.
- Decide about regular GitHub releases (e.g. yearly? or only when a "critial mass" is reached once it's more stable?)

## FAQ
### Mac build error
- If error `ERROR   -  "cairosvg" Python module is installed, but it crashed with:` just use:
- `export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` before. Or set it once, e.g. for zsh shell:
- `echo 'export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib' >> ~/.zshrc && source ~/.zshrc`

### Local installation
- best create virtual env with python 3.11 with 
- `pip install "mkdocs-material[imaging]==9.5.34"`
- `pip install mkdocs-glightbox mkdocs-minify-plugin mkdocs-git-revision-date-localized-plugin mkdocs-git-committers-plugin-2`
- `mkdocs serve` for local server or `mkdocs build` for the static html with assets

(See also github actions in .github/workflows/ci.yml)
