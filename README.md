# Python Mini Projects

A collection of small Python projects for practice, learning, and experiments.

## Repo Layout

Each mini project lives inside the `projects/` folder:

- `projects/automate-the-boring-stuff`
- `projects/caesar-cipher`
- `projects/project-template`
- `projects/time-travel`

When you add a new project later, create a new folder inside `projects/`.

## Starting A New Project

Use `projects/project-template` as your starter.

1. Copy the `project-template` folder.
2. Rename it to your new project name.
3. Update the new project's `README.md`.
4. Write your code in the `src/` folder.

Example new project names:

- `projects/number-guesser`
- `projects/todo-cli`
- `projects/password-generator`

## Working On A Project

1. Open this repo in PyCharm or VS Code.
2. Choose the project folder you want to work on.
3. If that project needs packages, create or activate its virtual environment.
4. Run the Python file for that project.

Example:

```bash
cd projects/project-template
python3 src/main.py
```

## Git Basics

When you make changes:

```bash
git status
git add .
git commit -m "Describe what changed"
git push
```

## Notes

- `.venv/`, `.idea/`, and cache files are ignored by Git.
- Keep project-specific notes in a small `README.md` inside each project folder.
