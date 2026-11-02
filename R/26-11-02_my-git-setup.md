# My Git setup (R)

What's set up on my Mac (MacBook Pro M3) and how the pieces connect. From my mac-setup steps of 06/10/26.

## The pieces

| Piece | What it is | How it talks to GitHub |
| --- | --- | --- |
| Ghostty | the terminal window | doesn't, it only shows the shell |
| tmux | splits Ghostty into panes, keeps sessions alive | doesn't, same as above |
| git | the version control program | pushes and pulls over HTTPS, using gh's login |
| gh (GitHub CLI) | GitHub from the terminal: clone, browse, PRs | logged in with `gh auth login` |
| Claude Code | Claude in the terminal | runs your own git and gh, so it uses the same login |
| Claude on claude.ai / desktop | Claude in the cloud | separate: through "Connect GitHub" and the Claude GitHub App |

So Ghostty and tmux don't need any GitHub setup. The only real link on the Mac is `gh auth login`.

## What `gh auth login` did

I answered: GitHub.com › HTTPS › Yes, authenticate Git with your GitHub credentials › Login with a web browser.

- gh saved a GitHub token in the macOS Keychain.
- "Yes, authenticate Git" made gh Git's password helper for github.com. That's why `git push` never asks for a password.
- Then I set the name and email that show on my commits with `git config --global user.name` / `user.email`.

## Check it still works

```
gh auth status
git config --global user.name
git config --global user.email
git config --global --get-regexp credential
```

The last one should mention `gh auth git-credential`. If it doesn't, `gh auth setup-git` fixes it.

## Claude in the cloud

Separate from the Mac. Claude reaches GitHub through:

- my GitHub account connected to Claude (claude.ai/connect-github)
- the Claude GitHub App installed on an account or org (github.com/apps/claude). On md-p2p-RAM it lets Claude push and open pull requests there.

Public repos can be read without either.

<!-- nav:footer -->

---

↑ [Home](../README.md) · [R](README.md)

<!-- /nav:footer -->
