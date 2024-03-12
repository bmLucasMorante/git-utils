import git
import os


def get_repo(repo_dir='.'):
    repo_dir = os.path.realpath(repo_dir)
    if not os.path.exists(repo_dir):
        raise ValueError('Path does not exists.')
    if not os.path.isdir(repo_dir):
        raise ValueError('Path is not directory.')
    return git.Repo(repo_dir)


def clone_repo(repo_url, repo_dir):
    git.Repo.clone_from(repo_url, repo_dir)
    os.chdir(repo_dir)
    return git.Repo(repo_dir)


def start_dev_config_branch(repo):
    repo.git.checkout('main', b='dev')
    repo.remotes.origin.pull()
    # Make dev-specific changes
    # Stage changes
    repo.git.add('.')
    # Commit changes
    repo.git.commit('-m', 'Dev-specific changes')
    # Push changes
    repo.remotes.origin.push('dev')


def start_dev_feature_branch(repo):
    repo.git.checkout('dev', b='dev.feature')
    # Make changes
    # Stage changes
    repo.git.add('.')
    # Commit changes
    repo.git.commit('-m', 'Feature changes')
    # Optionally squash commits
    # repo.git.rebase('--interactive', 'HEAD~2') # Replace 2 with the number of commits you want to squash
    # Push changes
    repo.remotes.origin.push('dev.feature')


def release_dev_feature_to_main(repo):
    repo.git.checkout('main')
    # List dev.feature commits excluding dev branch commits
    commits = repo.git.log('dev..dev.feature', '--oneline').split('\n')
    for commit in commits:
        sha = commit.split()[0]
        repo.git.cherry_pick(sha)
    # Tag the release
    repo.create_tag('v1.0')
    # Push changes
    repo.remotes.origin.push('main', tags=True)


def update_dev_branch(repo):
    repo.git.checkout('main')
    repo.git.rebase('dev', 'main')


def start_dev_featureX_branch(repo):
    repo.git.checkout('dev')
    repo.remotes.origin.pull()
    repo.git.rebase('dev', 'main')
    repo.git.checkout('dev')
    repo.git.branch('dev.featureX')
    repo.git.checkout('dev.featureX')


def release_dev_featureX_to_main(repo):
    # Optionally squash commits
    # repo.git.rebase('--interactive', 'HEAD~2') # Replace 2 with the number of commits you want to squash
    # Push changes
    repo.remotes.origin.push('dev.featureX')


def cleanup(repo_dir):
    os.chdir('..')
    shutil.rmtree(repo_dir)

# Example usage:
# repo_url = 'https://github.com/yourusername/config-repo.git'
# repo_dir = 'config-repo'
# repo = clone_repo(repo_url, repo_dir)
# start_dev_config_branch(repo)
# start_dev_feature_branch(repo)
# release_dev_feature_to_main(repo)
# update_dev_branch(repo)
# start_dev_featureX_branch(repo)
# release_dev_featureX_to_main(repo)
# cleanup(repo_dir)
