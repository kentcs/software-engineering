# Lecture 14: Software Maintenance and Evolution

## Introduction

Software engineering does not end when a system is deployed. In many cases, deployment is the moment when the longest phase of the system begins. Users discover defects, requirements change, external services evolve, dependencies become outdated, and code that once seemed clear becomes harder to work with. This is the domain of software maintenance and evolution.

SWEBOK treats software maintenance as a core engineering activity because real software systems continue to change after initial delivery. That framing also matches the Lecture 14 reading set on software maintenance, technical debt, and code refactoring, along with the relevant Head First Software Development chapters on good-enough design, testing, TDD, and ending an iteration well. The central idea is simple: software that survives must be changed, and engineering quality depends on how well those changes are controlled.

This chapter focuses on three core ideas:

- Corrective, adaptive, and perfective maintenance
- Refactoring in practice
- Technical debt
- Regression and impact analysis

These topics matter because a deployed system must continue to function in a changing environment. A team that can build software but cannot maintain it is not finished with the engineering problem.

## 1. What Software Maintenance Means

Students often hear "maintenance" and think only of bug fixing. In software engineering, maintenance is broader. It includes the modification of software after delivery in order to correct faults, improve quality, or adapt the software to new conditions.

This view is consistent with SWEBOK and the Wikipedia reading on software maintenance. The key point is that software maintenance is not accidental extra work added after the "real" project. It is part of the real project.

For a course project, maintenance might include:

- Fixing a collision bug in `sketch.js`
- Updating a Python route after a browser form changes
- Replacing a deprecated dependency
- Cleaning up duplicated logic so new features are easier to add
- Modifying deployment scripts after the server environment changes

Maintenance therefore includes both behavior changes and structure changes.

## 2. Why Evolution Happens

Software evolves because its context evolves.

Sources of change include:

- Defects discovered after release
- New user needs
- New browsers or runtime environments
- Changes in APIs, libraries, or hosting platforms
- Internal code quality problems that slow future work

In this sense, software evolution is normal rather than exceptional. The system is not broken simply because it needs to change. The real question is whether the system can absorb change without collapsing in quality.

For example:

- A P5.js app that worked in one browser may need updates when input handling changes
- A Python app that ran on one Linux server may need changes when moved to a different host or Python version
- A project that began as a class demo may need structural cleanup if the team wants to extend it into a larger system

## 3. Categories Of Maintenance

Lecture 14 centers on three major categories:

- Corrective maintenance
- Adaptive maintenance
- Perfective maintenance

These categories are useful because not all change requests are the same. A team should be able to explain not only what changed, but why it changed.

### Corrective Maintenance

Corrective maintenance fixes faults. It addresses behavior that is wrong relative to the intended system behavior.

Examples:

- A button click does nothing because the JavaScript event handler is broken
- A Python route returns the wrong output for a valid input
- A deploy succeeds, but the app crashes because a file path is incorrect

Corrective work is often urgent because users experience it as failure.

### Adaptive Maintenance

Adaptive maintenance changes the software so it continues to work in a changed environment.

Examples:

- Updating the app to run under a newer Python version
- Changing deployment logic when the Linux server path or port changes
- Replacing a library API call after the dependency deprecates the old one
- Modifying the app because a hosting platform now expects a different startup command

The system may have been correct before, but the world around it changed.

### Perfective Maintenance

Perfective maintenance improves the system even when it is not currently failing.

Examples:

- Making `sketch.js` easier to read and extend
- Splitting a large Python function into smaller helpers
- Improving error messages for users
- Reducing duplicated logic so future changes are less risky

Perfective work is often postponed because it does not look urgent, but it strongly affects long-term maintainability.

## 4. Maintenance Is Not A Side Task

One common mistake is to treat maintenance as an interruption to "real development." The software maintenance reading pushes against that view. Once software is used, maintenance becomes part of the normal lifecycle.

That matters because teams often under-plan for maintenance:

- They do not leave time for cleanup
- They postpone refactoring indefinitely
- They accept quick fixes that make future work worse
- They focus on visible features while internal quality declines

In practice, a mature engineering team expects ongoing maintenance and plans for it. Even a course project benefits from this mindset.

## 5. Refactoring In Practice

Refactoring is the disciplined restructuring of code without changing its externally visible behavior. The Wikipedia reading on code refactoring is important here because it distinguishes refactoring from feature development and bug fixing.

Refactoring is about internal design quality.

Typical goals include:

- Reducing duplication
- Improving naming
- Breaking apart large functions
- Making control flow easier to understand
- Clarifying module boundaries

For course projects, refactoring might look like:

- Extracting repeated collision logic from `sketch.js` into a helper function
- Moving repeated response formatting into a Python helper
- Renaming unclear variables such as `x1`, `x2`, and `temp3` to reflect real meaning
- Separating deployment-related constants from application logic

Refactoring is valuable because maintainability is partly structural. If the structure is weak, every future change becomes more expensive.

## 6. Refactoring Versus Other Changes

Students sometimes call every change a refactor, but that is not precise.

Examples:

- Fixing a bug is corrective maintenance, not automatically refactoring
- Adding a new feature is not refactoring
- Updating code to a new environment is adaptive maintenance
- Reorganizing code while preserving behavior is refactoring

Some changes combine multiple forms of work. For example, a team might fix a bug and also refactor the surrounding code while working in that area. That is common. The important point is to distinguish the purpose of each change.

This distinction matters in GitHub workflows. A pull request that says "refactor input handling" should not secretly change user-visible behavior unless that is explicitly stated. Clear maintenance categories improve communication as well as design.

## 7. Technical Debt

Technical debt is the cost imposed by choosing a quick or limited solution now that makes future change harder. The technical debt reading is useful because it gives students a language for discussing maintainability problems that do not show up as immediate failures.

Technical debt appears in many forms:

- Duplicated logic
- Weak naming
- Missing tests
- Fragile deployment scripts
- Manual server-only fixes
- Hard-coded paths, ports, or credentials assumptions
- Overly large files with mixed responsibilities

In a Python or JavaScript course project, technical debt can accumulate very quickly because the team is under schedule pressure and small shortcuts are easy to justify.

For example:

- Hard-coding a server port in multiple places
- Copying and pasting similar logic into several routes
- Keeping a huge `sketch.js` file with unrelated gameplay concerns mixed together
- Making manual edits on the Linux server instead of changing the repository
- Delaying cleanup because "the code works for now"

The danger is not that every shortcut is forbidden. The danger is losing track of the cost.

## 8. Debt Is A Tradeoff, Not A Moral Failure

Technical debt is often discussed too simplistically. Some debt is a conscious tradeoff. A team may choose a quick solution because a deadline is real and the system is low risk. That can be defensible.

The engineering problem is not "never incur debt." The real problem is:

- whether the team knows the debt exists
- whether the debt is documented
- whether the debt is growing faster than the team can control it

SWEBOK's engineering perspective is useful here. Engineering is about tradeoffs under constraints, not idealized purity.

For example, a class project may reasonably accept:

- a simpler file structure than a production system
- a lightweight deployment script
- limited test coverage in non-critical areas

But that same project should still recognize risky debt, such as no reproducible deployment process or no way to understand a large, tangled code file.

## 9. Maintenance In A GitHub-Centered Workflow

GitHub is relevant to Lecture 14 for the same reason it mattered in Lecture 13: the maintenance process should be visible and reviewable.

Useful GitHub-centered maintenance tools include:

- Git history for understanding when a problem appeared
- Pull requests for reviewing cleanup or bug-fix changes
- Issues for recording known defects and debt items
- GitHub Actions for running tests after maintenance changes
- TDD-style unit tests for locking in expected behavior before or during a fix
- BDD scenarios for checking user-visible behavior after maintenance changes
- Tags and release history for understanding when a regression entered production

In practice:

- A corrective maintenance PR might fix a broken Python route and add a regression test
- An adaptive maintenance PR might update a workflow after the server port changes
- A perfective maintenance PR might rename functions and simplify duplicated logic without changing behavior

In this course context, TDD and BDD are especially useful maintenance tools because they help teams control regression risk while code evolves:

- TDD helps developers write small tests around a failing behavior, fix the issue, and keep that bug from silently returning
- BDD helps teams express expected behavior from the user's point of view, which is useful when maintenance changes affect workflows rather than only isolated functions

GitHub does not perform the maintenance for the team, but it provides the control surface for doing maintenance responsibly.

## 10. Examples In Course Projects

Consider a few concrete cases.

### Example 1: Corrective Maintenance In P5.js

The ball in a bounce game passes through a wall because the collision condition is wrong.

Maintenance type:

- Corrective

Likely actions:

- Fix the condition in `sketch.js`
- Test the behavior manually
- Commit the change with a clear message
- Review the diff in GitHub

### Example 2: Adaptive Maintenance In Python

A Python app deployed on a Linux server fails after the runtime environment changes.

Maintenance type:

- Adaptive

Likely actions:

- Update dependency declarations
- Adjust startup or deployment commands
- Verify the app on the target server
- Record the environment-related change in the repository

### Example 3: Perfective Maintenance In Either Stack

The code still works, but one file has become too large and duplicated.

Maintenance type:

- Perfective

Likely actions:

- Extract helper functions
- Improve names
- Separate responsibilities
- Confirm behavior did not change

These examples matter because students often encounter all three forms of maintenance in the same week without naming them clearly.

## 11. Regression As A Maintenance Problem

Regression is one of the central risks in software maintenance. A regression happens when a change intended to improve or fix the system causes previously working behavior to stop working correctly.

This is why maintenance is hard. The problem is not only making the new change work. The problem is making the new change work without damaging everything around it.

Examples of regression in course projects include:

- Fixing collision logic in `sketch.js` but breaking score updates
- Cleaning up a Python route and accidentally changing its response format
- Updating deployment commands for a Linux server and unintentionally serving the wrong directory
- Replacing duplicated code with a helper and missing one edge case that the duplicated code previously handled

Regression matters because maintenance changes happen in an already-functioning system. The more useful software becomes, the more existing behavior there is to protect.

## 12. Impact Analysis

Impact analysis is the discipline of asking what else may be affected when a change is made.

This belongs directly inside software maintenance because most maintenance failures are not caused by misunderstanding the local fix. They are caused by misunderstanding the broader effect of the fix.

A practical impact-analysis process looks like this:

1. Identify the module, function, file, or interface being changed.
2. Check the modules directly connected to it.
3. Decide whether they are affected by the change.
4. If they are affected, continue outward to the modules connected to them.
5. Stop only when the effect no longer propagates.

This is essentially recursive change analysis across a dependency graph.

For example, suppose a Python route changes the format of the data it returns. The direct impact may be on the route handler itself, but the effect may continue into:

- helper functions that prepare the data
- frontend JavaScript that reads the response
- tests that assert the old format
- deployment or monitoring code that assumes a particular output

The first change is local. The impact is not.

### Direct And Transitive Impact

Students often check only direct dependencies. That is not enough.

A maintenance change can create:

- direct impact: the immediately connected module is affected
- transitive impact: other modules are affected through the modules in between

This is exactly why regression is often surprising. The code that fails may be several hops away from the code that changed.

### Transient Impact Through Data Flow

One of the most important maintenance ideas is that impact can propagate through data even when an intermediate module does not examine that data deeply.

For example, a module may:

- forward a parameter unchanged
- store a value temporarily
- wrap data in another structure
- filter or reorder records
- pass an event object to another layer

Even if that module does not "understand" the data semantically, it can still carry impact forward.

This is what might be called transient impact: the effect is transmitted through the system by data flow rather than by local business logic.

In course projects, this can happen when:

- a Python route changes JSON structure and frontend code later breaks
- a P5.js helper changes the meaning of a returned value and later calculations become wrong
- a deployment script changes a path or port that downstream commands simply pass along

### Why Impact Analysis Matters

Impact analysis helps a maintenance team decide:

- what needs review
- what needs testing
- what needs refactoring first
- what regressions are plausible

TDD, BDD, code review, and regression testing are not substitutes for impact analysis. They are ways to verify the impact analysis was correct or to catch what it missed.

## 13. Historical And Current Approaches To Managing Regression

Teams have always needed ways to control regression, but the techniques have changed over time.

### Historical Approaches

Older or less automated workflows often depended on:

- Careful manual testing by developers
- Written checklists of important behaviors
- Dedicated regression test passes before release
- Human reviewers comparing old and new behavior by inspection
- Slower release cycles so teams had time for broader manual verification

These approaches were not irrational. They reflected the tools available at the time and are still sometimes necessary today. For example, a visual P5.js interaction may still require a human to verify that the animation feels correct.

But historical approaches have limits:

- Manual checks are easy to forget
- People do not repeat the exact same steps consistently
- Coverage is usually uneven
- Fast release cycles make large manual test passes impractical

### Current Approaches

Modern teams try to manage regression with more automation and tighter feedback loops.

Common current approaches include:

- Automated unit tests
- Integration tests
- End-to-end or scenario-based tests
- Continuous integration runs on every pull request
- TDD-style regression tests added when bugs are found
- BDD scenarios for preserving user-visible behavior
- Smaller pull requests and smaller maintenance changes

In GitHub-centered workflows, this often means:

- opening a pull request for a maintenance change
- running automated checks through GitHub Actions
- reviewing both the code change and the regression protection added with it
- merging only after behavior is verified

The basic idea is to reduce the gap between "I made a change" and "I learned whether that change broke something important."

### Both Old And New Still Matter

It would be a mistake to think modern automation makes older methods obsolete.

In practice, good maintenance work often combines approaches:

- automated tests for repeatable checks
- BDD scenarios for user-facing behavior
- manual exploration for UI feel and unusual edge cases
- code review for design and maintainability concerns

For a class project, this mixed strategy is realistic. You may not have enterprise-scale automation, but you can still reduce regression risk substantially by combining tests, scenarios, manual checks, and disciplined pull request review.

## 14. Refactoring And Testing

Refactoring is safer when supported by testing. If the goal is to improve structure without changing behavior, the team needs some way to detect accidental regressions.

This does not require a massive test suite, but it does require discipline.

TDD and BDD are both relevant here.

TDD is useful when the team is working close to the code. A developer can reproduce a bug with a failing unit test, make the smallest code change that fixes it, and then keep that test as protection against regression. This is often a strong fit for Python functions, route handlers, and smaller pieces of game logic.

BDD is useful when the team wants to preserve externally visible behavior. A behavior-oriented scenario can describe what the user should experience before and after a maintenance change. This is especially helpful when maintaining workflows, UI interactions, or end-to-end application behavior.

Helpful patterns include:

- Running automated tests after refactoring
- Adding a TDD-style regression test when fixing a bug
- Using BDD scenarios for user-visible behavior that must remain stable
- Keeping manual test checklists for UI-heavy projects
- Comparing before-and-after behavior explicitly
- Refactoring in small steps rather than rewriting everything at once

For example, if a student extracts repeated helper logic from a Python file, tests or manual checks should confirm the routes still behave the same. A TDD-style unit test can lock in the expected output of a helper or route. If a student reorganizes `sketch.js`, the game should still respond the same way before additional changes are made. A BDD-style scenario can help verify that a user action still produces the expected visible result.

Refactoring without verification is often just risky rewriting.

## 15. Warning Signs Of Maintenance Trouble

A system is becoming hard to maintain when the team notices patterns such as:

- Small changes cause unrelated breakage
- Developers are afraid to touch certain files
- Bug fixes create new bugs
- Every feature requires copy-paste edits in many places
- The deployment or startup process is fragile and poorly understood
- The codebase accumulates TODO comments without resolution

These are not only coding problems. They are maintainability signals.

The software maintenance and technical debt readings are useful here because they encourage teams to see maintainability as a quality concern in its own right.

## 16. Practical Guidance

For a small or medium course project, a reasonable maintenance baseline is:

- Classify the kind of change you are making
- Fix bugs clearly and verify them
- Refactor in small, reviewable steps
- Record technical debt instead of pretending it does not exist
- Avoid manual server-side fixes that bypass version control
- Use GitHub pull requests to separate bug fixes, cleanup, and new features when possible

For this course, those habits can be translated into concrete behavior:

- If you fix a deploy problem, decide whether it is corrective or adaptive
- If you clean up `sketch.js`, say explicitly whether behavior should remain the same
- Before changing a module, ask what direct and transitive dependencies may be affected
- Track transient impact through data passed along between modules, even if intermediate code does not inspect it closely
- If you fix a bug, consider writing a TDD-style regression test first or immediately after reproducing it
- If the behavior matters from the user's point of view, describe it in a BDD-style scenario so the maintenance goal stays visible
- If the change touches UI behavior, use manual regression checks as a complement to automated tests
- If you take a shortcut, record the debt in an issue, comment, or follow-up task
- If you touch risky code, verify behavior before and after the change

These habits make future maintenance cheaper and clearer.

## Summary

Software maintenance and evolution are normal parts of software engineering, not cleanup after the interesting work is finished. SWEBOK emphasizes maintenance because deployed software must continue to change in response to defects, environmental shifts, and quality concerns.

The assigned readings support that view from complementary angles:

- the software maintenance reading explains why post-delivery modification is a core activity
- the refactoring reading explains how to improve internal structure without changing external behavior
- the technical debt reading explains why shortcuts create future costs
- Head First Software Development Chapter 5 connects maintenance to design quality and cleanup during normal development
- Head First Software Development Chapter 7 connects maintenance to testing and continuous integration as regression protection
- Head First Software Development Chapter 8 connects maintenance to TDD as a practical way to hold behavior steady while code changes
- Head First Software Development Chapter 9 connects maintenance to iteration wrap-up, bug fixing, and deciding what to improve before moving on
- Head First Software Development Appendix A reinforces refactoring as an ongoing maintenance skill

If a team can identify the kind of maintenance it is doing, improve code structure deliberately, and manage technical debt openly, it is treating software as an evolving engineered system rather than a one-time assignment.

## Discussion Questions

1. What is the difference between corrective, adaptive, and perfective maintenance?
2. Why is refactoring not the same thing as feature development?
3. When is technical debt a reasonable tradeoff, and when is it dangerous?
4. Why do maintainability problems often appear as process problems rather than only coding problems?
5. How can GitHub practices make maintenance work more disciplined and visible?

## References

- SWEBOK v4 summary and source listing in this repository: `SWEBOK/swebok-outline.md`
- SWEBOK full PDF: https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf
- Head First Software Development, Chapter 5: Good-Enough Design: Getting it done with great design
- Head First Software Development, Chapter 7: Testing and Continuous Integration: Things fall apart
- Head First Software Development, Chapter 8: Test-Driven Development: Holding your code accountable
- Head First Software Development, Chapter 9: Ending an Iteration: It’s all coming together...
- Head First Software Development, Appendix A: Leftovers: The top 5 topics (we didn’t cover)
  - Refactoring
- Wikipedia: Software Maintenance
  https://en.wikipedia.org/wiki/Software_maintenance
- Wikipedia: Technical Debt
  https://en.wikipedia.org/wiki/Technical_debt
- Wikipedia: Code Refactoring
  https://en.wikipedia.org/wiki/Code_refactoring
