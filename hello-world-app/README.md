## How to run locally (without Docker)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

## How to run with Docker
```bash
docker build -t hello-world-app .
docker run -d -p 5000:5000 --name hello-container hello-world-app
```
Visit http://localhost:5000

## Automated pipeline
Every push to `main` that touches this folder triggers a GitHub Actions
workflow (`.github/workflows/docker-build.yml`) that:
1. Checks out the code on a clean Ubuntu runner
2. Builds the Docker image from scratch
3. Runs the container and sends a real request to it with `curl`
4. Fails the build if the app doesn't respond correctly

This catches real integration problems (not just syntax errors) before
they reach anyone else working on the project.

## Issues encountered during development
- Initial `pip install` failed due to Ubuntu's externally-managed-environment
  protection — solved by using a Python virtual environment (`venv`)
  instead of installing packages system-wide.
- A typo (`prot` instead of `port`) in the Flask run call caused a runtime
  crash — fixed by correcting the argument name.
- GitHub rejected pushes to the workflow file until the Personal Access
  Token was regenerated with the `workflow` scope, since GitHub treats
  CI/CD config as higher-privilege than regular code.
- The workflow's `paths` filter meant pushing only the workflow file
  itself didn't trigger a run, since it only watches changes inside
  `hello-world-app/`. Had to push a change inside that folder to test it.
- The workflow YAML initially failed to parse due to inconsistent
  indentation (steps not aligned, a command accidentally split across
  two lines, and `jobs:` nested instead of being a top-level key) —
  fixed by rewriting the file with consistent 2-space indentation
  throughout.
