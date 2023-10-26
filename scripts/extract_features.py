# -*- coding: utf-8 -*-
import os
import sys
import csv
import datetime


def avg_time_between_commits(commits):
    total_commits_between_time = datetime.timedelta(0)
    commits_count = commits.count()
    if commits_count <= 0:
        return 0
    before_commit = commits.order_by('created_at')[0]
    for a_commit in commits.order_by('created_at')[1:]:
        total_commits_between_time += (a_commit.created_at - before_commit.created_at)
        before_commit = a_commit
    avg_commits_between_time = (total_commits_between_time / commits_count)
    days = avg_commits_between_time.days
    hours = (avg_commits_between_time.seconds / 3600)
    return ((days * 24) + hours) if days > 0 else hours


def avg_time_between_merged_prs(pull_requests):
    total_merged_prs_between_time = datetime.timedelta(0)
    merged_prs = pull_requests.filter(merged=True)
    merged_prs_count = merged_prs.count()
    if merged_prs_count <= 0:
        return 0
    before_pr = merged_prs.order_by('closed_at')[0]
    for a_pr in merged_prs.order_by('closed_at')[1:]:
        total_merged_prs_between_time += (a_pr.closed_at - before_pr.closed_at)
        before_pr = a_pr
    avg_merged_prs_between_time = (total_merged_prs_between_time / merged_prs_count)
    days = avg_merged_prs_between_time.days
    hours = (avg_merged_prs_between_time.seconds / 3600)
    return days * 24 + hours if days > 0 else hours


def avg_time_between_prs(pull_requests):
    total_merged_prs_between_time = datetime.timedelta(0)
    merged_prs = pull_requests
    merged_prs_count = merged_prs.count()
    if merged_prs_count <= 0:
        return 0
    before_pr = merged_prs.order_by('opened_at')[0]
    for a_pr in merged_prs.order_by('opened_at')[1:]:
        total_merged_prs_between_time += (a_pr.opened_at - before_pr.opened_at)
        before_pr = a_pr
    avg_merged_prs_between_time = (total_merged_prs_between_time / merged_prs_count)
    days = avg_merged_prs_between_time.days
    hours = (avg_merged_prs_between_time.seconds / 3600)
    return days * 24 + hours if days > 0 else hours


def avg_pr_life_time(pull_requests):
    total_prs_life_time = datetime.timedelta(0)
    prs_count = pull_requests.count()
    if prs_count <= 0:
        return 0
    for pr in pull_requests:
        if pr.opened_at and pr.closed_at:
            total_prs_life_time += (pr.closed_at - pr.opened_at)
    return (total_prs_life_time / prs_count).days


def avg_percentage_merged_prs_by_2_weeks(pull_requests):
    prs_order_by_opened_at = pull_requests.order_by('opened_at')
    if prs_order_by_opened_at.count() <= 0:
        return 0
    date_from = prs_order_by_opened_at[0].opened_at
    date_to = list(prs_order_by_opened_at)[-1].opened_at
    seek_date = date_from
    period_quantity = 0
    percentage_merged_prs = 0

    while seek_date < date_to:
        next_date = seek_date + datetime.timedelta(days=14)

        prs = pull_requests.filter(opened_at__lte=next_date, closed_at__gte=seek_date)
        total_prs_count = prs.count()
        merged_prs_count = prs.filter(merged=True, closed_at__gte=seek_date, closed_at__lte=next_date).count()
        if total_prs_count > 0:
            percentage_merged_prs += (merged_prs_count / total_prs_count)
            period_quantity += 1

        seek_date = next_date

    return (percentage_merged_prs / period_quantity) if period_quantity > 0 else 0


def median_time_between_commits(commits):
    tbcs = []
    if commits.count() <= 0:
        return 0
    before_commit = commits.order_by('created_at')[0]
    for a_commit in commits.order_by('created_at')[1:]:
        tbcs.append(a_commit.created_at - before_commit.created_at)
        before_commit = a_commit
    tbcs.sort()
    median = tbcs[int(len(tbcs) / 2)]
    days = median.days
    hours = (median.seconds / 3600)
    return ((days * 24) + hours) if days > 0 else hours


def median_time_between_merged_prs(pull_requests):
    tbpr = []
    merged_prs = pull_requests.filter(merged=True)
    merged_prs_count = merged_prs.count()
    if merged_prs_count <= 0:
        return 0
    before_pr = merged_prs.order_by('closed_at')[0]
    for a_pr in merged_prs.order_by('closed_at')[1:]:
        tbpr.append(a_pr.closed_at - before_pr.closed_at)
        before_pr = a_pr
    tbpr.sort()
    median = tbpr[int(len(tbpr) / 2)] if len(tbpr) > 0 else datetime.timedelta(days=0)
    days = median.days
    hours = (median.seconds / 3600)
    return days * 24 + hours if days > 0 else hours


def median_time_between_prs(pull_requests):
    tbpr = []
    merged_prs = pull_requests
    merged_prs_count = merged_prs.count()
    if merged_prs_count <= 0:
        return 0
    before_pr = merged_prs.order_by('opened_at')[0]
    for a_pr in merged_prs.order_by('opened_at')[1:]:
        tbpr.append(a_pr.opened_at - before_pr.opened_at)
        before_pr = a_pr
    tbpr.sort()
    median = tbpr[int(len(tbpr) / 2)] if len(tbpr) > 0 else datetime.timedelta(days=0)
    days = median.days
    hours = (median.seconds / 3600)
    return days * 24 + hours if days > 0 else hours


def median_pr_life_time(pull_requests):
    ltpr = []
    for pr in pull_requests:
        if pr.opened_at and pr.closed_at:
            ltpr.append(pr.closed_at - pr.opened_at)
    median = ltpr[int(len(ltpr) / 2)] if len(ltpr) > 0 else 0
    return median.days if median != 0 else 0


def median_percentage_merged_prs_by_2_weeks(pull_requests):
    prs_order_by_opened_at = pull_requests.order_by('opened_at')
    if prs_order_by_opened_at.count() <= 0:
        return 0
    date_from = prs_order_by_opened_at[0].opened_at
    date_to = list(prs_order_by_opened_at)[-1].opened_at
    seek_date = date_from
    pmpr = []

    while seek_date < date_to:
        next_date = seek_date + datetime.timedelta(days=14)

        prs = pull_requests.filter(opened_at__lte=next_date, closed_at__gte=seek_date)
        total_prs_count = prs.count()
        merged_prs_count = prs.filter(merged=True, closed_at__gte=seek_date, closed_at__lte=next_date).count()
        if total_prs_count > 0:
            pmpr.append(merged_prs_count / total_prs_count)

        seek_date = next_date

    pmpr.sort()
    return pmpr[int(len(pmpr) / 2)] if len(pmpr) > 0 else 0


def commiters_count(commits):
    commiters = set([])
    for commit in commits:
        commiters.add(commit.raw_data.get('author_id'))
    return len(commiters)


def get_conflicting_prs_count(pull_requests):
    from pairwise_conflict_dataset.models import PairwiseConflict
    from django.db.models import Q
    conflicting_prs_count = 0
    for pr in pull_requests:
        conflict_count = PairwiseConflict.objects.filter(Q(first_pull_request=pr) | Q(second_pull_request=pr)).count()
        if conflict_count > 0:
            conflicting_prs_count += 1
    return conflicting_prs_count


def number_prs_to_default_branch(a_project):
    return a_project.pull_requests.filter(base_branch__contains=a_project.default_branch).count()


def percentage_prs_to_default_branch(a_project):
    prs_default_branch = a_project.pull_requests.filter(base_branch__contains=a_project.default_branch).count()
    total_prs = a_project.pull_requests.count()
    return (prs_default_branch / total_prs) * 100.0 if total_prs > 0 else 0.0


def number_prs_intra_branch(pull_requests):
    return pull_requests.filter(intra_branch=True).count()

def percentage_prs_intra_branch(pull_requests):
    prs_intra_branch = pull_requests.filter(intra_branch=True).count()
    total_prs = pull_requests.count()
    return (prs_intra_branch / total_prs) * 100.0 if total_prs > 0 else 0.0


def average_prs_commits_number(pull_requests):
    total_prs = pull_requests.count()
    commits_by_prs = 0
    for pr in pull_requests:
        if pr.github_raw_data:
            commits_by_prs += pr.github_raw_data.get('commits', 0)    
    return (commits_by_prs / total_prs) if total_prs > 0 else 0.0


def average_prs_comments_number(pull_requests):
    total_prs = pull_requests.count()
    commits_by_prs = 0
    for pr in pull_requests:
        if pr.github_raw_data:
            commits_by_prs += pr.github_raw_data.get('comments', 0)
    return (commits_by_prs / total_prs) if total_prs > 0 else 0.0


def average_prs_changed_files_number(pull_requests):
    total_prs = pull_requests.count()
    commits_by_prs = 0
    for pr in pull_requests:
        if pr.github_raw_data:
            commits_by_prs += pr.github_raw_data.get('changed_files', 0)
    return (commits_by_prs / total_prs) if total_prs > 0 else 0.0


def average_prs_additions_number(pull_requests):
    total_prs = pull_requests.count()
    commits_by_prs = 0
    for pr in pull_requests:
        if pr.github_raw_data:
            commits_by_prs += pr.github_raw_data.get('additions', 0)
    return (commits_by_prs / total_prs) if total_prs > 0 else 0.0


def average_prs_deletions_number(pull_requests):
    total_prs = pull_requests.count()
    commits_by_prs = 0
    for pr in pull_requests:
        if pr.github_raw_data:
            commits_by_prs += pr.github_raw_data.get('deletions', 0)
    return (commits_by_prs / total_prs) if total_prs > 0 else 0.0


def generate_csv_report(projects_data):
    with open('projects_report_all_2.csv', 'w') as data_file:
        header = ['project name', 'project age', '# commits', '# PRs', '# merged PRs', '# rejected PRs',
                  'average time between commits', 'average PR life time', 'average PRs between time',
                  'average merged PRs between time',
                  'Average % merged PRs by 2 weeks', 'median time between commits',
                  'median PR life time', 'median PRs between time', 'median merged PRs between time',
                  'median % merged PRs by 2 weeks', '# commiters', 'language', 'number PRs to default branch',
                  'percentage PRs to default branch', 'number PRs intra branch', 'percentage PRs intra branch',
                  'forks', 'size', 'average commits by PR', 'average comments by PR', 'average changed files by PR',
                  'average additions by PR', 'average deletions by PR', '# pairwise conflicts',
                  '# conflicting merged PRs', '% conflicting merged PRs', '# conflicting rejected PRs', '% conflicting rejected PRs']
        csv_writer = csv.writer(data_file)
        csv_writer.writerow(header)
        for project_data in projects_data:
            csv_writer.writerow(project_data)


def main():
    from pairwise_conflict_dataset.models import Project
    projects = Project.objects.all().order_by('created_at')
    projects_data = []
    for project in projects:
        project_data = []

        project_data.append(project.name)
        project_data.append((datetime.datetime(2019, 6, 1).astimezone() - project.created_at).days)
        project_data.append(project.commits.count())
        project_data.append(project.pull_requests.count())
        project_data.append(project.pull_requests.filter(merged=True).count())
        project_data.append(project.pull_requests.filter(merged=False, closed_at__isnull=False).count())
        project_data.append(avg_time_between_commits(project.commits.all()))
        project_data.append(avg_pr_life_time(project.pull_requests.all()))
        project_data.append(avg_time_between_prs(project.pull_requests.all()))
        project_data.append(avg_time_between_merged_prs(project.pull_requests.all()))
        project_data.append(avg_percentage_merged_prs_by_2_weeks(project.pull_requests.all()))
        project_data.append(median_time_between_commits(project.commits.all()))
        project_data.append(median_pr_life_time(project.pull_requests.all()))
        project_data.append(median_time_between_prs(project.pull_requests.all()))
        project_data.append(median_time_between_merged_prs(project.pull_requests.all()))
        project_data.append(median_percentage_merged_prs_by_2_weeks(project.pull_requests.all()))
        project_data.append(commiters_count(project.commits.all()))
        # news
        project_data.append(project.language)
        project_data.append(number_prs_to_default_branch(project))
        project_data.append(percentage_prs_to_default_branch(project))
        project_data.append(number_prs_intra_branch(project.pull_requests.all()))
        project_data.append(percentage_prs_intra_branch(project.pull_requests.all()))
        project_data.append(project.github_raw_data.get('forks', 0) if project.github_raw_data else 0)
        project_data.append(project.github_raw_data.get('size', 0) if project.github_raw_data else 0)
        project_data.append(average_prs_commits_number(project.pull_requests.all()))
        project_data.append(average_prs_comments_number(project.pull_requests.all()))
        project_data.append(average_prs_changed_files_number(project.pull_requests.all()))
        project_data.append(average_prs_additions_number(project.pull_requests.all()))
        project_data.append(average_prs_deletions_number(project.pull_requests.all()))
        # pairwise conflicts
        project_data.append(project.get_pairwise_conflicts_count())
        conflicting_merged_prs_count = get_conflicting_prs_count(project.pull_requests.filter(merged=True))
        conflicting_rejected_prs_count = get_conflicting_prs_count(project.pull_requests.filter(merged=False, closed_at__isnull=False))
        prs_count = project.pull_requests.count()
        project_data.append(conflicting_merged_prs_count)
        project_data.append((conflicting_merged_prs_count / prs_count) * 100 if prs_count > 0 else 0)
        project_data.append(conflicting_rejected_prs_count)
        project_data.append((conflicting_rejected_prs_count / prs_count) * 100 if prs_count > 0 else 0)

        projects_data.append(project_data)
    generate_csv_report(projects_data)


if __name__ == "__main__":
    # Init Django environment
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pull_request_data_analysis.settings')

    import django
    django.setup()

    main()