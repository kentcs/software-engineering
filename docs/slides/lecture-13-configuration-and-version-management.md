# Lecture 13

Configuration and Version Management (Post-Deployment)

---

## Lecture Focus

- Versioning strategies
- Build and release concepts
- Traceability from commit to deployment

---

## Reading Selections

Lecture 13 readings:

- SWEBOK: Software Configuration Management
- Wikipedia: software configuration management
- Wikipedia: version control
- Wikipedia: continuous delivery
- Head First Software Development: Chapters 6, 6.5, and 7

---

## Why This Matters

After deployment, the problem is no longer just writing code.

The team must control:

- what changed
- what was built
- what was released
- what is currently running

---

## Software Configuration Management

SCM is the discipline of controlling software artifacts over time.

It includes:

- source code
- dependencies
- build scripts
- deployment workflows
- environment-specific settings

---

## Configuration Items

A configuration item is any artifact whose change can affect the system.

Examples:

- application code
- `requirements.txt` or `package.json`
- CI/CD workflow files
- deployment scripts
- server paths and environment variables

---

## Version Control As The Base Layer

Version control helps teams:

- track history
- compare changes
- collaborate safely
- recover previous states

But version control alone does not tell us what is live in production.

---

## Versioning Strategies

Common approaches:

- commit hashes
- release tags
- semantic versions
- date-based versions

The key requirement is consistency.

---

## Commit Hashes

Strengths:

- precise
- unique
- automatically available

Limits:

- hard for humans to discuss
- not ideal as the only release label

---

## Tags And Releases

A tag marks a specific repository state as important.

Examples:

- `v1.2.0`
- `release-2026-04-01`

Tags help teams talk about releases without ambiguity.

---

## Build vs Release

Build:

- transforms source into deployable output

Release:

- selects a version for distribution or deployment

You can build many times without releasing every build.

---

## Build Concerns

Reliable builds depend on:

- dependency control
- tool versions
- repeatable scripts
- stable environments
- known outputs

If the build is not repeatable, the release is weak.

---

## GitHub-Centered Release Control

GitHub often becomes the control surface for:

- pull requests
- workflow runs
- tags
- releases
- traceability from merge to deploy

Version control alone is not enough. The team still has to connect code, build, release, and runtime state.

---

## Post-Deployment Questions

Good engineering can answer:

- Which version is running?
- Which commit produced it?
- What changed since the last release?
- Can we rebuild it?
- Can we roll it back?

---

## Traceability

Traceability connects:

- a commit
- a build artifact
- a release record
- a deployment event
- a running system

This is how teams know what is actually live.

---

## Traceability Pipeline

```text
commit -> build -> release -> deploy -> verify
```

Each step should leave evidence behind.

---

## Lightweight Deployment Example

A simple workflow might:

- check out the repo
- copy files with `scp`
- run remote commands with `ssh`
- reload the server
- verify the result

Even this simple pipeline still needs traceability.

---

## `bounce` Workflow Example

Course example:

- `bounce/.github/workflows/deploy.yml`

In a standalone `bounce` repo, this should live at `.github/workflows/deploy.yml`.

This file defines deployment configuration, not just deployment commands.

---

## What That Workflow Encodes

- host: `cassini.cs.kent.edu`
- user: `bounce`
- remote directory: `/home/bounce/bounce`
- app port: `12345`
- secrets: `ID_RSA` and `KNOWN_HOSTS`

If those values change, deployment behavior changes.

---

## Why The Workflow Matters

The workflow is itself a configuration item.

It controls:

- what files are copied
- where they are copied
- how the app is started
- how the deploy is verified

That is Lecture 13 in practice.

---

## Workflow Shape

```yaml
TARGET="$USER@$HOST"
RUN="ssh $SSH_OPTIONS $TARGET"
COPY="scp $SSH_OPTIONS -r"
$COPY index.html style.css sketch.js README.md LICENSE "$TARGET:$REMOTE_DIR/"
$RUN "cd '$REMOTE_DIR' && export PORT=$PORT && python3 -m http.server \"$PORT\""
```

The key point is not the exact syntax.

The key point is that the deployment process is versioned and reviewable.

---

## Common Failure Modes

- manual server edits
- environment drift
- untracked dependency changes
- unclear release labels
- no record of deployed commit
- build steps that only work on one machine

---

## Practical Baseline

For a healthy small project:

- version the source and scripts
- tag meaningful releases
- keep builds repeatable
- record the deployed version
- avoid production-only changes

---

## Reading Map

Head First Software Development helps here by theme:

- Chapter 6: version control
- Chapter 6.5: build automation
- Chapter 7: testing and continuous integration

These fit the lecture's versioning, build, and traceability concerns.

---

## Takeaway

Configuration and version management make deployed software understandable.

If the team can identify the running version, reproduce the build, and explain the path from commit to production, then the process is under control.
