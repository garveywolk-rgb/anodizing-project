# GitHub Workflow (GitHub Desktop)

First time using Git, so this is the no-terminal version. The mental model: this folder lives
in two places: on my computer (local) and on GitHub.com (remote). I make changes locally, then
**commit** (save a snapshot with a note) and **push** (upload it).

## One-time setup
1. Make an account at github.com. Username = professional (e.g. `garveywolk`); it goes on my resume.
2. Install GitHub Desktop (desktop.github.com), sign in.
3. **File → Add Local Repository**, point it at this `anodizing-project` folder.
   (If Desktop says it isn't a repo yet, choose "create a repository" here instead.)
4. Publish to GitHub.com, keep it **public** so recruiters/scanners can see it.

## The loop I repeat
1. Do work (add data, photos, code).
2. Open GitHub Desktop, it lists what changed.
3. Write a short summary in the box (e.g. "Add B2 voltage batch data + plots").
4. Click **Commit to main**.
5. Click **Push origin** (top bar) to upload.

## Good commit messages
- "Add B0 baseline session data and coupon photos"
- "Add color-vs-voltage plot"
- "Update README with first findings"

Small, frequent commits beat one giant dump, the history itself tells the story of the project.

## What's tracked vs ignored
`.gitignore` keeps large raw image dumps and scratch files local. The code, processed dataset,
figures, and docs all go public. If I want a specific big file tracked anyway, I can override.
