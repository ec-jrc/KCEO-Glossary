# KCEO Glossary

## Contributions and Feedback
The KCEO Glossary is built for the EO community. Your feedback and ideas are fundamental for the further development of this glossary. PR's and contributions of any kind are highly welcomed. 

### Contribution Guide
coming soon

## Local installation
See the github actions in .github/workflows/ci.yml.

## FAQ
### Mac build error
If error `ERROR   -  "cairosvg" Python module is installed, but it crashed with:` just use:

`export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` before. Or set it once, e.g. for zsh shell: 

`echo 'export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib' >> ~/.zshrc && source ~/.zshrc`

