# Lecture 13: Configuration and Version Management

## Introduction

Once software has been deployed, the engineering problem changes. The team is no longer only writing code. It is now responsible for controlling change, reproducing working versions, and explaining what is running in production. This is the domain of configuration and version management.

Software Configuration Management (SCM) is concerned with identifying software artifacts, controlling changes to them, and maintaining integrity across versions and releases. In practice, that includes source files, dependencies, build outputs, environment-specific settings, deployment workflows, and release records.

This framing matches the SWEBOK treatment of software engineering as a discipline that must design, build, test, deploy, and maintain software systems over time, not just write code once. It also lines up with the Lecture 13 reading set on Software Configuration Management, Version Control, and Continuous Delivery, along with the relevant Head First Software Development chapters on version control, build automation, and continuous integration.

This chapter focuses on three core ideas:

- Versioning strategies
- Build and release concepts
- Traceability from commit to deployment

These topics matter because a deployed system is only maintainable if the team can answer basic operational questions with confidence:

- Which version is running?
- What changed between releases?
- Can we rebuild the same version?
- Which commit introduced the behavior now in production?

## 1. What Counts As Configuration

Students often assume configuration means only a `.env` file or a few settings. In software engineering, the idea is much broader. A configuration item is any artifact that matters to building, running, testing, or releasing the system.

This broad definition is consistent with Software Configuration Management as described in both SWEBOK and the Wikipedia overview of software configuration management: the goal is not only to store files, but to identify and control the artifacts that define the system.

Typical configuration items include:

- Source code
- Dependency definitions
- Build scripts
- Test configuration
- Deployment workflows
- Runtime environment variables
- Infrastructure scripts
- Documentation tied to release behavior

If a change to an artifact can affect system behavior, it belongs in the conversation about configuration management.

For the kinds of projects used in this course, configuration items might include:

- A Python web app file such as `bottle_app.py`
- Frontend files such as `index.html`, `style.css`, and `sketch.js`
- A dependency file such as `requirements.txt` or `package.json`
- A GitHub Actions workflow such as `bounce/.github/workflows/deploy.yml`
- A Linux server path such as `/home/bouncer/mysite`
- An environment variable telling the app which database or API key to use

Notice that not all of these are "code" in the narrow sense. A workflow file or deployment target path can change the behavior of the system just as much as a Python function can.

## 2. Version Control As The Foundation

Version control is the base layer of configuration management. A repository records change over time and gives the team a structured way to collaborate, inspect history, and recover prior states.

The Lecture 13 Wikipedia reading on version control is useful here because it emphasizes that version control is about managing evolving states of a system, not merely keeping backups.

Version control supports several essential engineering activities:

- Comparing one version of a system with another
- Reverting a bad change
- Reviewing the exact content of a release
- Coordinating work across multiple developers
- Connecting defects to the code that introduced them

Without version control, there is no reliable way to reason about system evolution. With it, the team gains a timeline of change, but that alone is still not enough. A repository can tell us what changed, but not automatically which version was built, released, and deployed.

In a GitHub-centered workflow, version control usually includes:

- A Git repository hosted on GitHub
- Branches for ongoing work
- Pull requests for review and discussion
- Commit history for tracing defects and features
- Tags and releases for naming important versions

For example, if a student changes collision logic in `sketch.js` for a P5.js app, GitHub records exactly which lines changed and who changed them. If the deployment later behaves incorrectly, the team can inspect the pull request and the commit history instead of guessing.

## 3. Versioning Strategies

Versioning is the practice of assigning meaningful identifiers to system states. These identifiers help developers, testers, maintainers, and operators refer to the same release without ambiguity.

This section connects the version control reading to the larger SCM problem: once many valid repository states exist, teams need a disciplined way to name the ones that matter.

Common strategies include:

- Commit-based identification
- Tagged releases
- Semantic versioning
- Date-based release numbers

### Commit-Based Identification

Every commit hash identifies a unique repository state. This is precise and machine-friendly, but it is not always easy for people to communicate about. Saying "production is on commit `4f82c1a`" is accurate, but not especially descriptive for stakeholders.

In GitHub, the commit hash is automatically available in workflow runs. This makes it possible to say, "The Linux server is running the code produced by this exact commit," which is a strong traceability claim.

### Tagged Releases

Teams often create tags such as `v1.3.0` or `release-2026-04-01`. A tag marks an important commit and gives it a stable human-readable label. Tags are useful when a specific repository state has been approved for release or deployment.

For a class project, a tag might mark milestones such as:

- `v0.1.0` for the first deployable Python app
- `v0.2.0` after adding sound and animation to a P5.js game
- `release-demo-day` for the version shown in class

### Semantic Versioning

Semantic versioning uses identifiers like `MAJOR.MINOR.PATCH`.

Example:

- `2.0.0` indicates a breaking change
- `2.1.0` indicates backward-compatible added functionality
- `2.1.1` indicates a backward-compatible fix

This strategy is most useful when the software has consumers who need to reason about compatibility.

### Choosing A Strategy

There is no single universal versioning scheme. The important point is consistency. A weak but consistently applied version strategy is better than an elaborate strategy used inconsistently.

For a small GitHub-hosted course project, a practical strategy is:

- Use branches for day-to-day work
- Merge reviewed changes into the main branch
- Tag versions that are actually deployed
- Record the deployed tag or commit in release notes or workflow output

## 4. Build Concepts

A build is the process that transforms source materials into something that can be tested, packaged, or deployed. Depending on the system, the output might be:

- Compiled binaries
- Bundled frontend assets
- Packaged libraries
- Container images
- Static site files
- Deployment archives

The build process should be deterministic enough that the team can explain how an output was produced. If two developers cannot reproduce the same result from the same source state, the build process is weak.

This connects directly to the continuous delivery reading. Continuous delivery depends on repeatable builds and predictable automation; without that, there is no trustworthy path from source code to releasable software.

For course projects, builds may be fairly light:

- A Python app may not require compilation, but it still depends on the right interpreter version and installed packages
- A P5.js project may mostly consist of static files, but the "build" still includes assembling the correct HTML, JavaScript, CSS, and asset files for deployment

Even when the build feels simple, it is still a build process because the team is preparing a specific set of files to run on a Linux server.

Important build concerns include:

- Dependency resolution
- Toolchain versions
- Build scripts
- Build environment consistency
- Artifact naming and storage

The more manual a build is, the harder it becomes to trust and repeat.

Examples:

- A Python app may depend on `bottle` being installed on the server; if `requirements.txt` is missing or outdated, the build is not reproducible
- A JavaScript/P5.js app may depend on a specific directory of assets such as sound files; if someone forgets to copy that directory, the deployed version is incomplete
- A Linux server may run Python 3.11 while a student tested locally on Python 3.9, producing subtle runtime differences

## 5. Release Concepts

A release is not exactly the same thing as a build. A build is an output. A release is a decision and a controlled event. It means the team has selected a version to distribute or deploy.

The Wikipedia reading on continuous delivery is especially relevant here because it separates the ability to produce release-ready software from the business decision of when to release it.

A release process often includes:

- Selecting a commit or tag
- Building artifacts
- Running tests and checks
- Recording release notes
- Approving the release candidate
- Deploying the chosen version

This distinction matters because teams can build many times per day without releasing every build.

On GitHub, the release process is often supported by:

- Pull requests for approving changes before merge
- GitHub Actions for running checks automatically
- Tags for marking the chosen version
- GitHub Releases for attaching notes to a version

In other words, GitHub can serve as both the history system and the control panel for releases.

## 6. Post-Deployment Thinking

Once software is deployed, configuration management becomes more operational.

The team must track:

- The repository version
- The built artifact version
- The deployed environment
- The live runtime behavior

If these are not connected, debugging becomes guesswork. A deployed system without traceability forces engineers to ask basic questions by inspection instead of by process.

Consider a Python app on a Linux server:

- The repository says one thing
- The server files may say another
- The running process may be using a stale file until it is reloaded

Or consider a P5.js project:

- The local repository may include a new `sketch.js`
- The server may still be serving the older file
- The browser may be showing cached behavior unless the correct file was actually deployed

Post-deployment thinking means the team must reason about the real running system, not just the repository.

## 7. Traceability From Commit To Deployment

Traceability means we can follow a line from source change to running software.

This is where the three readings come together. Software configuration management gives the control structure, version control gives the history, and continuous delivery gives the repeatable path through build and release.

A strong traceability chain often looks like this:

1. A commit enters the repository.
2. A workflow builds or prepares deployable output.
3. The workflow records which commit produced the output.
4. A release identifier is assigned.
5. Deployment sends that version to a target environment.
6. The deployed system can be associated back to the commit and release record.

This is the engineering answer to the question, "How do we know what is running?"

Traceability reduces confusion during:

- Bug investigations
- Rollbacks
- Audits
- Maintenance handoffs
- Release retrospectives

In GitHub, traceability is strengthened when the team can connect:

- a pull request
- the merge commit
- the GitHub Actions workflow run
- the deployment target
- the live server behavior

## 8. A Simple Example Using SSH And SCP Workflows

In a small project, traceability may be built around a lightweight deployment process rather than a large platform. For example, a GitHub Actions workflow can:

- Check out a repository
- Use `scp` to copy files to a server
- Use `ssh` to run remote verification commands
- Touch or restart server-side application files

Even in this simple model, the important engineering question is not just "Did the copy succeed?" It is also:

- Which commit triggered the workflow?
- Which files were copied?
- Which environment received them?
- How do we verify the live system matches that change?

That is configuration management in practice.

In the course deployment pattern, the workflow might copy files such as:

- `index.html`
- `sketch.js`
- `style.css`
- `bottle_app.py`
- a directory such as `Sound_Effects/`

Then it may run remote Linux commands such as:

```bash
ssh user@host 'pwd'
ssh user@host 'whoami'
scp sketch.js user@host:/home/bouncer/mysite
ssh user@host 'touch /var/www/bouncer_pythonanywhere_com_wsgi.py'
```

This example is useful because it shows that deployment is not magic. It is a controlled sequence of file transfers and remote commands, and each step can be recorded and reviewed in GitHub Actions.

Students should read this section together with the continuous delivery article. Even though this course uses a lightweight `ssh` and `scp` workflow rather than an enterprise deployment platform, the same core idea applies: changes should move through a repeatable, visible process rather than ad hoc manual copying.

## 8.5 Example: The `bounce` Workflow File

The repository now includes a concrete example at:

- `bounce/.github/workflows/deploy.yml`

That path is shown from the perspective of this course repository. The intended standalone-repository form is `.github/workflows/deploy.yml` at the root of the `bounce` repo. In other words, if `bounce` is its own GitHub repository, the `.github` directory belongs at the base of that repository.

That file is a useful Lecture 13 artifact because it is both a deployment mechanism and a configuration item. If the workflow changes, the behavior of the deployed system changes.

The workflow defines:

- the deployment host: `cassini.cs.kent.edu`
- the deployment user: `bounce`
- the remote directory: `/home/bounce/bounce`
- the application port: `PORT=12345`
- the SSH secrets source: `ID_RSA` and `KNOWN_HOSTS`

It also encodes the deployment process itself:

1. Check out the repository.
2. Install the SSH key from GitHub Secrets.
3. Define helper commands for `ssh` and `scp`.
4. Create the target directory on the Linux server.
5. Stop any existing `screen` session for the app.
6. Remove previously deployed files that will be replaced.
7. Copy the application files and `docs/` to the server.
8. Start a new HTTP server in a named `screen` session using `PORT=12345`.
9. Run remote verification commands such as `pwd`, `whoami`, and `ls -la`.

An abbreviated version of the workflow looks like this:

```yaml
env:
  HOST: cassini.cs.kent.edu
  USER: bounce
  REMOTE_DIR: /home/bounce/bounce
  PORT: "12345"

- name: Install SSH key
  uses: shimataro/ssh-key-action@v2
  with:
    key: ${{ secrets.ID_RSA }}
    known_hosts: ${{ secrets.KNOWN_HOSTS }}

- name: Deploy application files
  run: |
    TARGET="$USER@$HOST"
    RUN="ssh $SSH_OPTIONS $TARGET"
    COPY="scp $SSH_OPTIONS -r"
    $COPY index.html style.css sketch.js README.md LICENSE "$TARGET:$REMOTE_DIR/"
    $COPY docs "$TARGET:$REMOTE_DIR/"
    $RUN "cd '$REMOTE_DIR'; screen -dmS '$SCREEN_NAME' bash -lc 'export PORT=$PORT && python3 -m http.server \"$PORT\"'"
```

This example illustrates several Lecture 13 points at once.

First, it shows traceability. The workflow runs from a GitHub repository state, so the deployment is tied to a specific commit and workflow run.

Second, it shows configuration management. The host, user, directory, port, and SSH behavior are all part of the deployed system configuration, even though they are not application logic.

Third, it shows build and release discipline in a lightweight form. Even without containers or a packaging system, the team still controls which files are copied, how the server is restarted, and how the deployment is verified.

Fourth, it shows why GitHub Actions is relevant to this lecture. The workflow is not separate from version management. It is version-managed itself, reviewed in GitHub, and executed from GitHub.

Students should also notice the repository layout assumption. GitHub Actions only discovers workflow files from `.github/workflows/` at the repository root. So for a standalone `bounce` repository, this example must be installed as `bounce/.github/workflows/deploy.yml` from the outside, or simply `.github/workflows/deploy.yml` from inside the `bounce` repository itself.

## 8.6 Relevant Tools In A GitHub-Based Workflow

If GitHub is the center of the team's process, several tools become especially relevant.

### Core Versioning Tools

- `git` for commits, branches, merges, and tags
- GitHub repositories for remote hosting and collaboration
- GitHub pull requests for review and controlled integration
- GitHub Releases for human-readable release records

### Build And Verification Tools

- GitHub Actions for automated workflows
- `pytest` for Python tests
- `npm` for JavaScript dependency and script management when needed
- `pip` and `requirements.txt` for Python dependency control

### Deployment Tools

- `ssh` for remote Linux commands
- `scp` for copying files to a server
- Linux shell commands such as `ls`, `pwd`, `whoami`, and `touch`

### Why These Tools Matter

These tools support different parts of the same control problem:

- `git` and GitHub tell us what changed
- Actions tells us what ran
- tags and releases tell us what version was intended
- `ssh` and `scp` tell us what reached the server

When used together, they provide a lightweight but defensible process.

## 9. Common Failures In Configuration Management

Many production problems are not caused by new algorithms or complex code. They come from weak control of versions and environments.

Common failures include:

- Manual edits on the server that are not reflected in the repository
- Dependencies changing without being pinned or recorded
- Multiple environments drifting apart
- Releases being described informally instead of tagged
- No record of which commit is live
- Build steps that only work on one developer's machine

These failures are process failures as much as technical failures.

This is also a SWEBOK-style point. The problem is not just defective code. It is loss of control over the configuration state of the system.

Concrete course examples include:

- A student edits `bottle_app.py` directly on the Linux server to "fix it quickly," but the change is never committed to GitHub
- A workflow copies `index.html` and `sketch.js` but forgets the `Sound_Effects/` directory
- One machine installs a newer Python package version, but `requirements.txt` was not updated
- The team deploys from `main` without a tag, and later cannot say exactly which state was used for the demo
- A workflow run succeeds, but the remote app is not reloaded, so the server still serves older Python code
- The `bounce/.github/workflows/deploy.yml` file is edited to change `PORT`, `REMOTE_DIR`, or the copied files, but the team does not realize this changed the deployment behavior

## 10. Engineering Tradeoffs

Configuration management always involves tradeoffs.

A strict process improves reproducibility and safety, but adds overhead. A lightweight process is faster, but easier to misuse. Good engineering requires choosing enough process to maintain control without making the team unable to move.

Questions to ask include:

- How expensive is failure in this system?
- How often do releases happen?
- How many people modify the software?
- How much auditability is required?
- How quickly must the team be able to roll back?

The right answer for a classroom project is not always the right answer for a medical, financial, or safety-critical system.

## 11. Practical Guidance

For a small or medium software project, a reasonable baseline is:

- Keep all source and deployment scripts in version control
- Tag releases deliberately
- Make builds repeatable
- Record which commit is deployed
- Avoid manual production-only changes
- Use automation for repeated release steps

This does not eliminate risk, but it makes the system understandable.

For this course, that baseline can be translated into concrete habits:

- Keep `.github/workflows/` in the repository, not just local shell scripts
- Commit `requirements.txt`, `package.json`, or other dependency records
- Use pull requests instead of pushing major changes blindly
- Tag versions that are actually demonstrated or deployed
- Let GitHub Actions perform repetitive deployment steps where possible
- Treat the Linux server as a deployment target, not as the place where development happens

## Summary

Configuration and version management are about disciplined control of change after software becomes real in the world. Version control records history, build processes generate deployable outputs, release processes choose which outputs matter, and traceability connects source changes to live systems.

If a team can identify the exact version of its software, reproduce how it was built, and explain how it reached production, then it has the essentials of sound configuration management.

The assigned readings support this summary from different angles:

- SWEBOK provides the engineering view of controlling software artifacts over time
- the software configuration management article provides terminology and scope
- the version control article explains the change-history foundation
- the continuous delivery article explains why reproducible build and release pipelines matter
- Head First Software Development Chapter 6 connects these ideas to day-to-day defensive use of version control
- Head First Software Development Chapter 6.5 emphasizes build automation and repeatable project setup
- Head First Software Development Chapter 7 connects testing and continuous integration to keeping the system releasable

## Discussion Questions

1. Why is a commit hash precise but sometimes insufficient as a release identifier?
2. What is the difference between a build and a release?
3. Why does post-deployment traceability matter more than simple source history?
4. What risks appear when engineers edit production systems manually?
5. How much process is appropriate for a class project compared with a high-risk system?

## References

- SWEBOK PDF: https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf
- Head First Software Development, Chapter 6: Version Control: Defensive development
- Head First Software Development, Chapter 6.5: Building your Code: Insert tab a into slot b...
- Head First Software Development, Chapter 7: Testing and Continuous Integration: Things fall apart
- Wikipedia: Software Configuration Management
  https://en.wikipedia.org/wiki/Software_configuration_management
- Wikipedia: Version Control
  https://en.wikipedia.org/wiki/Version_control
- Wikipedia: Continuous Delivery
  https://en.wikipedia.org/wiki/Continuous_delivery
