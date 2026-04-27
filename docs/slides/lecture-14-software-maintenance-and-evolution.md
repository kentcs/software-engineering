# Lecture 14

Software Maintenance and Evolution

---

## Focus

- corrective, adaptive, and perfective maintenance
- refactoring in practice
- technical debt
- regression and how to manage it
- impact analysis

---

## The Point

Software that survives gets changed.

The issue is not whether change will happen.

The issue is whether the team can change the system without making it worse every time.

---

## Why This Matters

Deployment is not the end of the engineering problem.

After release, teams still have to:

- fix faults
- adapt to new environments
- improve structure
- avoid breaking working behavior

---

## What Maintenance Means

Software maintenance is modification after delivery.

It includes:

- bug fixing
- adaptation to change
- quality improvement
- structural cleanup

---

## Course Examples

- fixing a bug in `sketch.js`
- updating a Python route
- replacing a deprecated dependency
- adjusting a deployment script
- cleaning up duplicated logic

---

## Why Software Evolves

Software changes because its context changes.

Typical course examples:

- a bug shows up after demo day
- a server upgrade changes runtime behavior
- a dependency gets deprecated
- the team tries to add one feature and discovers the file is a mess

---

## Three Maintenance Categories

- corrective: fix faults
- adaptive: respond to environmental change
- perfective: improve quality and maintainability

The categories help explain why a change is being made.

---

## Corrective Maintenance

Corrective maintenance fixes wrong behavior.

Examples:

- broken event handler
- wrong route output
- bad file path after deploy

Users experience corrective issues as failures.

---

## Adaptive And Perfective

Adaptive example:

- the app worked on one server, then fails after a Python or host change

Perfective example:

- the app still works, but one file has become big enough to ruin everyone's day

---

## Refactoring

Refactoring changes structure without changing external behavior.

Typical goals:

- reduce duplication
- improve clarity
- separate responsibilities
- make future change safer

---

## Refactoring Distinctions

Important distinction:

- bug fix != automatically a refactor
- new feature != refactor
- environment update != refactor
- restructuring while preserving behavior = refactor

---

## Technical Debt

Technical debt is the future cost of a quick or limited solution now.

Examples:

- duplicated code
- missing tests
- fragile deployment scripts
- hard-coded ports or paths
- giant mixed-responsibility files

---

## Debt As A Tradeoff

Debt is not always irrational.

The real questions are:

- do we know it exists?
- did we choose it intentionally?
- is it getting harder to control?

Untracked debt is the real problem.

---

## Regression

A regression happens when a change breaks behavior that used to work.

Maintenance is difficult because the team must:

- make the new change work
- keep existing behavior working

---

## Regression Examples

- fix wall collision, break scoring
- clean up a route, change response format
- update deployment, serve the wrong directory

---

## Impact Analysis

Impact analysis asks:

- what else could this change affect?
- which connected modules may now be wrong?
- how far does the effect propagate?

Maintenance work fails when teams analyze only the local fix.

---

## Direct And Transitive Impact

- direct impact: immediately connected code is affected
- transitive impact: impact continues through other modules

A regression may appear several hops away from the changed code.

---

## Transient Impact Through Data

Impact can travel through data that is passed along without much examination.

- forwarding a parameter
- wrapping or storing a value
- filtering or reordering records
- passing events or payloads downstream

The middle module may not "understand" the data, but it can still carry the impact.

---

## Historical Regression Control

Older and less automated approaches relied on:

- manual testing
- written checklists
- dedicated regression passes
- human review and comparison
- slower release cycles

These still matter, especially for UI-heavy behavior.

---

## Current Regression Control

Modern teams add tighter feedback loops:

- unit tests
- integration and end-to-end tests
- CI on pull requests
- TDD-style regression tests
- BDD scenarios
- smaller maintenance changes

The best teams usually mix both approaches instead of pretending one replaced the other.

---

## TDD And BDD

TDD helps when working close to the code:

- reproduce bug with a failing test
- fix it
- keep the test to prevent regression

BDD helps preserve user-visible behavior:

- express expected behavior as a scenario
- verify workflows and outcomes from the user's view

---

## GitHub-Centered Maintenance

Useful tools and habits:

- Git history
- pull requests
- issues for defects and debt
- GitHub Actions
- regression tests in the same PR
- review of both the fix and the protection

---

## Refactoring And Testing

- run tests after refactoring
- add a regression test when fixing a bug
- use BDD for visible workflows
- keep manual checks for UI behavior
- refactor in small steps

---

## Warning Signs

- small changes cause unrelated breakage
- developers fear certain files
- bug fixes create new bugs
- copy-paste edits are common
- startup or deploy behavior is fragile
- TODOs accumulate without resolution

These are maintainability signals.

---

## Practical Baseline

For a healthy course project:

- say what kind of maintenance this is
- do impact analysis before touching risky code
- verify the fix and the old behavior around it
- refactor in small reviewable steps
- record debt instead of normalizing it
- avoid manual server-only fixes

---

## Reading References

- SWEBOK: Software Maintenance
- Wikipedia: software maintenance
- Wikipedia: technical debt
- Wikipedia: code refactoring
- Head First Software Development: Chapters 5, 7, 8, 9, and Appendix A on refactoring

These support the maintenance, regression, and refactoring parts of the lecture.

---

## Takeaway

Software maintenance is normal engineering work.

A disciplined team can:

- explain what kind of maintenance it is doing
- improve structure deliberately
- manage debt openly
- control regression while the system evolves
