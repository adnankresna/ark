# Mode detection

Inspect the current working directory. Decide which mode you're in. **Be conservative.** If anything looks unsafe, pause and ask before touching the layout.

## Greenfield mode

The directory is effectively empty. None of:
- PRDs, strategy docs, decks
- Interview transcripts, research notes
- Roadmap files, spec docs
- Prior `.md` files describing the product, strategy, team
- Substantial subfolders that look like an existing knowledge base

A `.git/`, a stray `README.md`, or empty subfolders do not count as PM artifacts.

**Action:** announce greenfield mode. Run the full 5-batch interview (see `interview.md`).

## Migration mode

The directory contains pre-existing PM artifacts (decks, transcripts, strategy docs, prior notes) and otherwise looks like a notes/working folder.

**Action:**
1. Announce migration mode. List what you found in one line: "I see X files matching PM artifact patterns (decks, transcripts, strategy docs, prior knowledge)."
2. Load `migration.md` and run the migration workflow before the interview. **Default to copy, never move.**

## Active-repo mode — pause and ask

The directory looks like an **active working repository**, not a notes folder. Signals (any of):

- `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, `Gemfile`, or other build/manifest files at the root.
- `src/`, `lib/`, `app/`, `tests/`, `node_modules/`, `vendor/`, `target/`, `dist/`, `build/` folders.
- `.git/` with non-trivial history (commits older than today, multiple authors, remotes configured).
- CI config (`.github/workflows/`, `.gitlab-ci.yml`, `circle.yml`, etc.).
- `Dockerfile`, `docker-compose.yml`, infra-as-code.
- Substantial source code in any language.

**Do not scaffold without confirmation.** Pause and ask:

> "This directory looks like an active working repository (detected: <list signals>). I can:
> (a) scaffold the PM Brain here alongside the existing files (recommended only if you intend to keep PM context with this project),
> (b) abort — you `cd` into a different directory and re-run.
> Which one?"

Do not proceed until the operator answers. Never silently scaffold over an active repo. The skill does not change directories on its own; the operator picks the project root by where they invoke it.

## Edge cases

- **Directory has artifacts but they're clearly someone else's project** (a `package.json` for a React app, but no PM artifacts): treat as active-repo mode and ask.
- **Mixed:** the user pasted a setup request with attached files but the directory is empty. Treat the pasted artifacts as migration inputs even though the FS is empty. Confirm with the PM before copying anything into `source/`.
- **Ambiguous:** ask one clarifying question before proceeding. Mode choice changes the whole workflow downstream — don't guess.

## Announce mode in one line

Greenfield:
> "Greenfield mode. Empty directory. Running the full 5-batch interview."

Migration:
> "Migration mode. Found 1 strategy doc, 3 interview transcripts, 2 decks, 4 prior stakeholder notes. I'll **copy** these into `source/` (originals stay put) and run a narrowed interview."

Active-repo (after operator confirms (a)):
> "Scaffolding PM Brain alongside the existing repo. Migration: found N PM artifacts mixed in with source code — I'll copy only PM-pattern files into `source/`, ignoring code/build directories."
