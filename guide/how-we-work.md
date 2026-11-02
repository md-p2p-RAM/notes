# How we work

Five rules. They keep three people from overwriting each other.

1. **Pull before you start.** `git pull` gets the others' changes and the bot's updates.
2. **Write in your own folder** (A, M or R). Shared files at the root (02_pensar, 04_crear, README) have one editor at a time: say it in the group chat before you edit one.
3. **Commit small, with a clear message,** starting with your letter: `R: add night moodboard`.
4. **Push right away.** If Git refuses, `git pull`, then `git push` again.
5. **Never force-push.** `git push --force` deletes the others' work.

## Names

- Notes: `yy-mm-dd_topic.md`, lowercase, hyphens, no spaces or accents. Example: `26-11-02_chalet-pierre-tournante.md`.
- First line of every note is `# Title`. That title is what shows in the index.
- Dates inside notes: dd/mm/yy.

## Links between notes (the Obsidian part)

- Link with normal Markdown and a relative path: `[Pensar](../02_pensar.md)`. It works on GitHub and in Obsidian.
- In Obsidian, `[[wikilinks]]` are off on purpose (settings are in `.obsidian/app.json`), so new links come out in the Markdown form above.
- After each push, a bot rebuilds the index on the home page and adds "Linked from" at the bottom of each note. Don't edit between the `nav` markers, it gets overwritten.

## Images

- Put them in your folder's `img/` (Obsidian does this for you when you paste an image).
- JPG, about 2000 px wide, under 1 MB. In the Terminal: `magick in.png -resize 2000x -quality 75 out.jpg`.
- Side by side on GitHub: two `<img src="img/a.jpg" width="48%">` on the same line.
- No splats, videos or zips here: `.gitignore` blocks them. Link to them instead.

## Open as an Obsidian vault

Obsidian → Open folder as vault → pick the cloned `notes` folder. Obsidian runs natively on Apple Silicon.

<!-- nav:footer -->

---

↑ [Home](../README.md)  
Linked from: [md-p2p-RAM · notes](../README.md)

<!-- /nav:footer -->
