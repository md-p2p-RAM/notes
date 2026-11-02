# Git in the Terminal, 10 min

A reminder of what each command does and when to type it. Everything runs in Ghostty (or any terminal), inside tmux if you like.

## The idea

There are two copies of the notes: **yours** (a folder on your Mac) and **GitHub's** (the shared one). Git moves changes between them.

- `pull` = GitHub → your Mac
- `push` = your Mac → GitHub
- `commit` = a saved snapshot on your Mac, with a message. Nothing leaves your Mac until you push.

```
your edits  →  git add  →  git commit  →  git push  →  GitHub
                                           git pull  ←  GitHub
```

## Once per Mac

```
git config --global pull.rebase false
```
Tells Git: when my copy and GitHub's both changed, merge them. Without it, `git pull` stops and asks how to reconcile.

```
cd ~/Documents
gh repo clone md-p2p-RAM/notes
cd notes
```
`clone` downloads the whole repo into a new folder called `notes`. You only do this once. From then on, `cd ~/Documents/notes` to get back in.

## Every time you work

| Step | Command | What it does |
| --- | --- | --- |
| 1 | `git pull` | Gets what the others (and the bot) pushed. Always first. |
| 2 | edit your notes | In Obsidian, VS Code, anything. |
| 3 | `git status` | Lists what you changed. Red = not added yet, green = added. |
| 4 | `git diff` | Shows the exact lines you changed. `q` to quit. |
| 5 | `git add R/` | Picks what goes into the next snapshot. `git add .` = everything you changed. |
| 6 | `git commit -m "R: add moodboard notes"` | Saves the snapshot on your Mac, with a message. |
| 7 | `git push` | Sends your snapshots to GitHub. |

Short version, when you know what you changed:

```
git pull
git add .
git commit -m "R: what I did"
git push
```

## When something goes wrong

**Push refused** ("rejected", "fetch first"): someone pushed before you. Run `git pull`, then `git push`. Normal, happens often because the bot commits after each push.

**Conflict** (after a pull: "CONFLICT ... Automatic merge failed"): you and someone else changed the same lines. Git puts both versions in the file:

```
<<<<<<< HEAD
your version
=======
their version
>>>>>>> origin/main
```

Open the file, keep what you want, delete the three marker lines. Then:

```
git add .
git commit -m "R: merge"
git push
```

Panic button, before you've committed the merge: `git merge --abort` puts everything back as it was before the pull.

**Undo**

- `git restore file.md` throws away your changes to a file since the last commit. Can't be undone.
- `git restore --staged file.md` un-adds a file (keeps your changes).
- `git log --oneline` lists recent snapshots. `q` to quit.

**Never** `git push --force`. It replaces GitHub's copy with yours and deletes what the others pushed.

## Looking at things

- `git log --oneline -10` the last 10 snapshots.
- `git show <id>` what one snapshot changed (the id is the short code from the log, like `3c85c2e`).
- `gh browse` opens the repo on github.com. `gh browse R/README.md` opens one file.

## tmux, quick

tmux splits one Ghostty window into panes and keeps your session alive when you close the window.

| Keys | Does |
| --- | --- |
| `tmux new -s notes` | start a session called notes |
| ⌃B then % | split left / right |
| ⌃B then " | split top / bottom |
| ⌃B then an arrow | move between panes |
| ⌃B then D | detach (session keeps running) |
| `tmux a -t notes` | come back to it |

A handy layout: Claude Code or your editor on the left, a pane for `git status` / `git pull` / `git push` on the right.

<!-- nav:footer -->

---

↑ [Home](../README.md)  
Linked from: [md-p2p-RAM · notes](../README.md)

<!-- /nav:footer -->
