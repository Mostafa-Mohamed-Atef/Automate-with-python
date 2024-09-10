#!/usr/bin/env python3

import subprocess
import sys

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8').strip(), error.decode('utf-8').strip(), process.returncode

def main():
    # Fetch the latest changes from the remote
    run_command("git fetch")

    # Get the current branch name
    branch_name, _, _ = run_command("git branch --show-current")

    # Check if there are any incoming changes
    incoming_commits, _, _ = run_command(f"git rev-list HEAD..origin/{branch_name} --count")

    if int(incoming_commits) > 0:
        print("WARNING: There are incoming changes. Please pull before committing.")
        sys.exit(1)

if __name__ == "__main__":
    main()