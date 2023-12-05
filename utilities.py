"""Utilities module."""
import os


def get_current_path():
    """Returns current path for the caller file."""
    return os.path.dirname(os.path.realpath(__file__))


def get_data_from_file(rel_file_path):
    """Reads and returns data from file.
       Path is relative to caller file location."""
    file_name = f"{get_current_path()}/{rel_file_path}"
    with open(file_name, encoding="utf-8") as reader:
        data = reader.read()
    return data


def get_github_api_headers(token):
    """Returns a dictionary with a set of headers for GitHub API access with specified `token`."""
    return {"Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28"}
