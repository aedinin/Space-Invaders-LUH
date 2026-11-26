# Contributing

Space Invaders - GIP Spieleprojekt (WiSe 26/27).
Terminal game in Python 3, standard library only.

New to branches or Pull Requests? Don't worry - just follow the flow below.
If anything looks weird or you get stuck, ask in the group chat **before**
running any `--force` command.

## Setup

- **Python 3.10+** (`python` or `py` on Windows, `python3` on Linux/macOS)
- **No third-party packages.** Everything uses the standard library.
- Run the game from the project root:

      python main.py

- **Controls:** `ENTER` start, `LEFT`/`RIGHT` move, `P` pause/resume, `Q` quit
- **If the terminal looks broken** (cursor hidden, no echo after a crash):
  the game restores it automatically on a normal exit. If it ever does not,
  type `reset` on Linux/macOS, or open a new terminal tab on Windows.

## Daily Workflow

1. **Always start from an up-to-date `main`:**

       git switch main
       git pull

2. **Create a branch for your task** - never work directly on `main`
   (older git: `git checkout -b feature/short-name`):

       git switch -c feature/short-name

   > **Already started coding on `main`?** As long as you have not committed
   > yet, `git switch -c feature/short-name` moves your uncommitted changes to
   > the new branch safely.

3. **Code and test locally:**

       python main.py

   `main.py` imports every module, so syntax and import errors show up at start.

4. **Commit and push:**

       git add .
       git commit -m "module: what changed"
       git push -u origin feature/short-name

5. **Open a Pull Request on GitHub** (base: `main`).
   One PR = one feature or fix. Drop the link in the group chat.

## Merging a PR

Anyone except the author should verify the branch and merge it. If nobody is
available, merge it yourself and say so in the chat - do not leave a PR open
for days.

To test someone else's branch locally:

    git fetch origin
    git switch feature/short-name
    python main.py

Then use **Rebase and merge** (the dropdown arrow next to the green button):

- **Why Rebase?** It keeps the original author on every commit, so `git log`
  shows who wrote what. This matters for our presentation.
- **Do not use *Squash and merge*:** the squashed commit is credited to whoever
  clicked the button, and the real author only survives as `Co-authored-by`.
- *Create a merge commit* also works but adds a merge node per PR; we keep the
  history linear.
- After merging, click **Delete branch**, and set the task on the to-do sheet
  from `To do` to `Done`.

Branch author, after the merge (note the capital `-D`: rebased commits get new
hashes, so `-d` refuses):

    git switch main
    git pull
    git branch -D feature/short-name

## Never

- **Never push directly to `main`.** Branch + PR, always. Direct pushes caused
  our rejected pushes and one abandoned branch in week 1.
- **Never `git push --force`.** It deletes other people's commits permanently.
- **Never commit `.vs/`, `__pycache__/` or `*.pyc`.** `.gitignore` already
  covers them; do not bypass it.
- **Keep source files ASCII only.** Chinese characters or German umlauts get
  saved as GBK by Windows and then either crash Python or show up as garbage on
  GitHub. This bit us twice already.

## Commit Messages

Format: `module: what changed`

**Modules:** `input`, `render`, `game`, `config`, `states`, `docs`, plus any new
ones (`entities`, `waves`, `combat`, ...).

- Good: `input: treat movement keys as held state` , `render: draw the alien grid`
  , `config: add KEY_HOLD_TIMEOUT`
- Avoid: `update`, `fix`, `wip`

When the reason is not obvious, add a body:

    git commit -m "input: add POSIX backend" -m "msvcrt is Windows-only, so the game had no keyboard on Linux."

## Merge Conflicts

    git fetch origin
    git rebase origin/main

`git status` lists the files with conflicts. Open each one and delete the
`<<<<<<<`, `=======`, `>>>>>>>` lines, keeping both sides where both changes
matter. Then:

    git add <file>
    git rebase --continue

If an editor (vim) opens: press `Esc`, type `:wq`, press `Enter`.
To give up and start over: `git rebase --abort`.

## Where things live

    main.py          entry point only
    game/game.py     Game class: loop, state machine, update, render
    game/input.py    keyboard -> action names (Windows: msvcrt, POSIX: termios)
    game/render.py   character grid -> terminal output
    game/states.py   State enum + next_state()
    game/config.py   every tunable constant