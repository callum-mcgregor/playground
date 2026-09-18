## Contributing to this repository

This repository utilises [Release Please](https://github.com/googleapis/release-please) 
```
Release Please automates CHANGELOG generation, the creation of GitHub releases, and version bumps for your projects.

It does so by parsing your git history, looking for Conventional Commit messages, and creating release PRs.
```

Use conventional commit messages: https://www.conventionalcommits.org/en/v1.0.0/
- To release a patch version (X.Y.Z+1):
  - `fix: `
  - Any other prefix that isn't `feat: `
- To release a minor version (X.Y+1.0):
  - `feat: `
- To release a major version (X+1.0.0):
  - `fix!: `
  - `feat!: `
  - Or any other prefix that includes an exclaimation point


> [!NOTE] Admittedly this repository is just a playground, but it's still a handy tool to track changes
> and I want to improve my understanding of the tool.

See ./release-please.md for more information