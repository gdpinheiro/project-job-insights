from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    with open(f"{path}", encoding="utf-8") as file:
        jobs_list = []
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs_reader:
            jobs_list.append(job)
        return jobs_list
