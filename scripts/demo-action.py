import git
import sys


def update_dev_branch(repo_dir="."):
    # print(f"[DUMMY] git rebase dev, main", repo_dir)
    # print(repo)
    repo = git.Repo(repo_dir)
    for each in repo.heads:
        print(each)
    # repo.git.checkout('main')
    # repo.git.rebase('dev', 'main')


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python update_dev_branch.py <repo_dir>")
    #     sys.exit(1)

    # repo_dir = sys.argv[1]
    update_dev_branch()
