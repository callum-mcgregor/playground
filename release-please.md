## release-please notes

Notes for understanding and utilising the release-please tool

```
Release Please automates CHANGELOG generation, the creation of GitHub releases, and version bumps for your projects.

It does so by parsing your git history, looking for Conventional Commit messages, and creating release PRs.
```

### How it works

The release-please repo has a great breakdown in the [What's a Release PR? section](https://github.com/googleapis/release-please#whats-a-release-pr)

### Prerequisites

#### PR merge strategy
It's highly recommended to use squash-merges with release-please [ref](https://github.com/googleapis/release-please#linear-git-commit-history-use-squash-merge)
so I've disallowed any merge strategy other than squash-merges.

I also updated the default commit message for squash-merges to be the Pull request title & description.
This has two benefits:
1. Only PR title must be linted for release-please 
2. Commits on `main` the PR description for additional information

#### PR title linting
Because we use squash-merges, the PR title becomes the commit message on
`main` - release-please reads that commit message to decide on the version
bump and changelog entry. So every PR targeting `main` must have a valid 
Conventional Commit message title.

To enforce this, the `.github/workflows/lint-pr-title.yml` workflow automatically
lints every PR's title to ensure it follows Conventional Commit rules.
