## TODO
- Set base aliases hook
  - git utils install
    - scripts
      - git-list-branches
      - install-config <repo> <path>
      - git-update-dev
      - git-new-dev.feature <newFeatureName>
      - git-release-feature <featureName>
    - git wrapper aliases
- Set user aliases hook
  - user defined aliases

### Install Process
The idea is to have a way to easily setup the developer workstation. needs:
- python 3.9.13
- git + git credentials -token
- google drive desktop mounted at G:
- Onboarding:
  - company email
  - github/gitlab account -token for now
  - sg account
    - add user to pipeline configurations (primary, dev, dev.<username>)
  - clone codebase
    - .venv
      - sg libs?
    - studio pipeline repos
      - git-utils
- SG toolkit Desktop
- setup local SG config
  - check Liju's meeting notes
- install-shell-scripts.bat

## Description

Shell scripts for developers to aid and streamline workflow.

To use this batch file:

Save the provided code as git-utils.bat.
Place it in a directory that's included in your system's PATH environment variable.
Open a command prompt in your Git repository directory.
Use the aliases defined in the batch file, such as git-clone-dev, git-dev-branch, etc., followed by any necessary parameters.

## Examples

initial setup:
```commandline
# Start inital setup
git clone config-repo
git checkout main
git pull

# start dev config branch
git branch dev (create dev branch)
git checkout dev
git commit dev-specific changes
git push

# Start dev.feature branch
git branch dev.feature
git checkout dev.feature
git commit
git commit
git squash (cleanup)
git push (optional but recomemnded, good for code review and backup)

# release dev.feature to main
git checkout main
list dev.feature commits (make sure we dont get the dev(parent branch) commits/changes)
git cherry-pic found-comits in cronological order
git tag
git push

# Update dev branch to include the dev.feature updates.
git checkout main
git rebase dev onto main

# New dev.featureX
git checkout dev
git pull
git rebase dev onto main
git branch dev.featureX
git checkout dev.featureX

# release dev.featureX to main (replay feature commits on top of main, optionally do a cleanup of commits before this process w/ git squash)
git squash (optional)
git checkout main
list dev.featureX commits (make sure we dont get the dev(parent branch) commits/changes)
git cherry-pic found-comits in cronological order
git tag
git push

```

Dev workflow:
```


git-clone-dev <config_repo_url>
git-dev-branch
git-dev-fetch
git-dev-push
```

release setup:
```
git-create-release-branch 1.0.0
git-tag-release 1.0.0 "Release version 1.0.0"
git-release-push
```
