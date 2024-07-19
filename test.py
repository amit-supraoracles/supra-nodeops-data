import subprocess

def git_update(repo_path, commit_message="committing signatures"):
    try:
        # Navigate to the repository directory
        subprocess.check_call(["cd", repo_path], shell=True)

        # Execute git pull
        subprocess.check_call(["git", "pull"], cwd=repo_path)

        # Add changes to staging
        subprocess.check_call(["git", "add", "."], cwd=repo_path)

        # Commit changes
        subprocess.check_call(["git", "commit", "-m", commit_message], cwd=repo_path)

        # Push changes to the master branch
        subprocess.check_call(["git", "push", "origin", "master"], cwd=repo_path)

        print("Git operations completed successfully.")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing git commands: {e}")

# Example usage
repo_path = "/home/codezeros/Videos/0MS/supra-nodeops-data"
git_update(repo_path)

