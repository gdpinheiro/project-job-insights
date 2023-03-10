from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    jobs_list = read(path)

    job_types = set()

    for job in jobs_list:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """

    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)

    industry_types = set()

    for industry in jobs_list:
        if industry["industry"] != "":
            industry_types.add(industry["industry"])

    return industry_types


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_industries = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_industries.append(job)

    return filtered_industries


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    jobs_list = read(path)

    max_salary = set()

    for salary in jobs_list:
        if salary["max_salary"] != "":
            try:
                max_salary.add(float(salary["max_salary"]))
            except ValueError:
                print("ValueError")

    max_salary = max(max_salary)

    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    min_salary = set()

    for salary in jobs_list:
        if salary["min_salary"] != "":
            try:
                min_salary.add(float(salary["min_salary"]))
            except ValueError:
                print("ValueError")

    min_salary = min(min_salary)

    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary doesn't exist")

    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("min_salary or max_salary aren't valid integers")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")

    elif type(salary) != int:
        raise ValueError("salary isn't a valid integer")

    salary = job["min_salary"] <= salary <= job["max_salary"]

    return salary


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """

    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            print("ValueError")

    return filtered_jobs
