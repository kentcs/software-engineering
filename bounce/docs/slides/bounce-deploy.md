# Deploying Bounce to Cassini

This deck covers the practical steps needed to publish the static Bounce app behind `bounce.kentcs.org` on Cassini.

---

## Goal

- Copy the static app to the server
- Start a persistent HTTP server on port `15999`
- Make the process easy to stop and restart
- Keep deployment repeatable through GitHub Actions
- Let Nginx terminate HTTPS and proxy traffic to the local app

---

## What The App Needs

- Static files only
- No backend runtime
- One web server command on the remote host
- A stable directory on the server where the app lives
- Nginx in front of the app, listening on the public hostname

The current app is just HTML, CSS, JavaScript, and CDN-loaded p5.js.

---

## Recommended Deployment Flow

1. Push code to GitHub
2. Trigger a manual GitHub Actions workflow
3. SSH into Cassini with the repo private key
4. Sync the repository contents to the remote directory
5. Restart the `screen` session that runs the HTTP server
6. Let Nginx continue serving `https://bounce.kentcs.org` and proxy to port `15999`

---

## Workflow Sections

The workflow file is easiest to understand in these parts:

- manual trigger
- workflow inputs
- key generation
- server key install
- GitHub secret storage
- runner SSH file setup
- job environment values
- command variables
- copy step
- start and stop steps

Each section has one job: move the static app to the server and restart the HTTP service cleanly.

---

## Workflow Inputs

The workflow should ask for:

- SSH username
- Remote directory to serve
- SSH port, if different from `22`

These inputs keep the workflow reusable across accounts and directories.

---

## Initial Setup Sequence

1. Generate the key pair with `ssh-keygen`
2. Install the public key on Cassini with `ssh` and `vi ~/.ssh/authorized_keys`
3. Put the private key into the GitHub secret named `ID_RSA`
4. Run the manual dispatch workflow

That sequence gets the server, the secrets store, and the runner aligned before the first deploy.

---

## Generate Keys

On a machine with `ssh-keygen`, create a key pair:

```bash
ssh-keygen -t ed25519 -C "bounce deploy"
```

The private key stays private. The public key is what you install on the server.

---

## Install Public Key

SSH into Cassini directly, then append the public key to `~/.ssh/authorized_keys`.

```bash
ssh your-user@cassini.cs.kent.edu
vi ~/.ssh/authorized_keys
```

Paste the public key on its own line, save the file, and make sure the permissions stay strict.

---

## Store Private Key

Put the private key contents into the GitHub secret named `ID_RSA`.

The workflow reads that secret and writes it to `~/.ssh/id_rsa` on the GitHub Actions runner.

---

## Runner SSH Files

The GitHub Action should create these local files on the runner:

- `~/.ssh/id_rsa`
- `~/.ssh/known_hosts`

That lets `ssh` and `scp` use the same local SSH setup without relying on an agent.

---

## Key Lifecycle

```text
local machine
  |
  v
ssh-keygen creates key pair
  |
  +--> public key -> Cassini ~/.ssh/authorized_keys
  |
  +--> private key -> GitHub secret ID_RSA
                          |
                          v
                 GitHub Actions runner ~/.ssh/id_rsa
                          |
                          v
                     ssh / scp to Cassini
```

The private key stays in the secret store, while the public key is what the server trusts.

---

## Command Variables

Inside the deploy step, define reusable shell variables:

```bash
SSH_OPTIONS="-i ${HOME}/.ssh/id_rsa -o IdentitiesOnly=yes -o BatchMode=yes -o StrictHostKeyChecking=yes -p ${REMOTE_PORT}"
RUN="ssh ${SSH_OPTIONS} ${REMOTE_USER}@${REMOTE_HOST}"
COPY="scp ${SSH_OPTIONS} -r"
STOP="${RUN} 'screen -S ${SCREEN_NAME} -X quit'"
START="${RUN} 'screen -dmS ${SCREEN_NAME} bash -lc ...'"
```

`SSH_OPTIONS` carries the SSH flags, `RUN` builds remote SSH commands, `COPY` builds SCP commands, and `STOP`/`START` manage the named `screen` session.

If you need to delete remote files or directories, use `RUN rm ...` so the removal happens on Cassini itself.

---

## Required Secrets

Store the SSH private key as a GitHub secret named `ID_RSA`.

If you manage allowed keys separately, keep that on the server side as the authorized public keys file.

Nginx certificates are managed separately with certbot for each hostname you provision.

---

## Remote Server Prep

On Cassini, make sure:

- The destination directory exists
- Your SSH key is authorized
- `screen` is installed
- Python 3 is available
- the public key is present in `~/.ssh/authorized_keys`
- Nginx has a dedicated config file for `bounce.kentcs.org`
- Certbot has issued the TLS certificate for that hostname

Without those pieces, the workflow can copy files but not keep the server running.

---

## Sync Step

Use `COPY` to send the static files to Cassini with `scp`.

For this repo, the deploy step copies:

- `index.html`
- `style.css`
- `sketch.js`
- `README.md`
- `LICENSE`
- `docs`

That keeps the deployment focused on the static app files.

---

## Cleanup Step

Use `RUN rm ...` for files or directories that should be removed on the server before or during deploy.

That is the right tool for deletion because it runs the command remotely instead of transferring files.

---

## Server Process

Run the app with:

```bash
python3 -m http.server 15999
```

This serves the files in the chosen directory over HTTP for Nginx to proxy to.

The `START` command creates the named `screen` session and launches that server.

The `STOP` command kills the same session before the new one starts.

---

## Why Use `screen`

- The server keeps running after SSH disconnects
- The session can be killed cleanly
- The same session name can be reused on every deploy

A fixed session name makes restart behavior predictable.

---

## Session Naming

Use one explicit session name, such as:

```text
bounce-static-http
```

Deployment should:

- stop that session if it already exists
- start a fresh session with the same name

---

## Port Choice

Serve the app on port `15999`.

That gives you a stable local port for Nginx to proxy to while the public site stays on HTTPS.

---

## Request Flow

```text
browser
  |
  v
DNS: bounce.kentcs.org
  |
  v
Nginx on Cassini (HTTPS)
  |
  v
HTTP app on localhost:15999
  |
  v
web server serving the app files
```

This could be a static server, Flask, Streamlit, NodeJS/Express, or any other HTTP server.

The key requirement is simple: the app must listen on its assigned port and speak HTTP to Nginx.

---

## Verification

After deployment:

- open `https://bounce.kentcs.org`
- confirm the canvas loads
- confirm the static assets and CDN scripts load correctly

If the page is blank, check browser dev tools, the Nginx config, the certbot certificate, and the remote `screen` session.

---

## Common Failure Points

- SSH key is missing or not authorized
- Remote directory path is wrong
- `screen` is not installed
- Port `15999` is not reachable from Nginx
- Python is not available as `python3`
- Nginx server block is misconfigured
- TLS certificate is missing or expired

Most deployment issues show up quickly in the workflow logs or the remote terminal.

---

## Rollback

If a deploy is bad:

1. Kill the `screen` session
2. Restore the previous files on the server
3. Re-run the workflow with the last known good commit

Because the app is static, rollback is usually just a file copy problem.

---

## Summary

Deployment for Bounce is simple:

- generate a key pair with `ssh-keygen`
- install the public key on Cassini with `vi ~/.ssh/authorized_keys`
- store the private key in the `ID_RSA` secret
- let the GitHub Action create `~/.ssh/id_rsa` and `~/.ssh/known_hosts`
- use `SSH_OPTIONS`, `RUN`, `COPY`, `START`, and `STOP`
- sync static files with `scp`
- start `python3 -m http.server 15999`
- keep it alive in a named `screen` session
- manage the process through manual GitHub Actions
- let Nginx expose the site at `https://bounce.kentcs.org`
