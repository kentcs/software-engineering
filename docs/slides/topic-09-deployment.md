# Deployment

Moving a built application from a repository to a running server.

---

## What Deployment Means

Deployment is the step where code stops being just source files and becomes a running system on a target machine.

Common goals:

- Put the right files on the right server
- Restart or refresh the application
- Verify the deployed version matches the commit

---

## Why This Topic Matters

Deployment is where engineering decisions become visible to users.

- A good build is not useful if it never reaches production
- A bad deployment can break a working build
- Traceability matters when debugging release problems

---

## The Basic Path

```text
commit -> build -> copy files -> run remote commands -> verify
```

That is the core deployment loop used by many small projects.

---

## SSH And SCP

Two common tools show up in simple deployment workflows:

- `ssh` runs commands on a remote machine
- `scp` copies files to a remote machine

Together, they let a workflow push code and trigger a restart.

---

## The Pattern In `./bounce`

The `./bounce/.github/workflows/` directory shows a practical pattern:

- Install an SSH key on the GitHub Actions runner
- Check out the repository
- Copy files with `scp`
- Run remote commands with `ssh`
- Restart the remote service cleanly

---

## Example Workflow Shape

```yaml
- name: Install SSH key
  uses: shimataro/ssh-key-action@v2

- name: Deploy application files
  run: |
    $RUN "set -eu; mkdir -p '$REMOTE_DIR'"
    $COPY index.html style.css sketch.js README.md LICENSE "$TARGET:$REMOTE_DIR/"
    $RUN "set -eu; cd '$REMOTE_DIR'; screen -dmS '$SCREEN_NAME' bash -lc 'cd \"$REMOTE_DIR\" && export PORT=$PORT && python3 -m http.server \"$PORT\"'"
```

The details vary, but the structure is stable.

---

## What Gets Deployed

In the `./bounce` workflow, deployment sends application assets like:

- `index.html`
- `sketch.js`
- `style.css`
- `README.md`
- `LICENSE`
- `docs/`

This is a file-based static-site deployment, not a container build.

---

## Remote Verification

Good workflows do not assume success.

Typical checks:

- `ls -la`
- `pwd`
- `whoami`
- Restart the remote process
- Open the site and confirm the new behavior

---

## Traceability

Traceability means you can connect:

- A commit
- A build artifact
- A deployment event
- A running version on a server

This is what lets you answer, "What is live right now?"

---

## Version Management

Deployment works better when files are versioned deliberately.

- Tag releases when you need a stable reference
- Keep build outputs separate from source when possible
- Record which commit produced the deployed version

---

## Release Risks

Deployment failures usually come from predictable causes:

- Missing files on the server
- Wrong SSH credentials
- Stale remote state
- Reload not triggered
- Environment mismatch between local and remote

---

## A Simple Checklist

Before deploying:

- Build the app successfully
- Confirm the target host and user
- Copy only the needed files
- Run a remote sanity check
- Verify the live server after the workflow completes

---

## Takeaway

Deployment is a controlled transfer from development state to production state.

If you can explain:

- what is copied
- how the server is updated
- and how you verify the result

then you understand the practical deployment pipeline.
