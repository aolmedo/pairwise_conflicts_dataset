# -*- coding: utf-8 -*-
import os
import sys
import csv
import datetime
import subprocess
import re


def main():
    from pairwise_conflict_dataset.models import Project
    projects = Project.objects.all()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    project_dir = '{}/projects'.format(parent_dir)
    regex = '.*\s+(?P<files>\d+)\s+(?P<blank>\d+)\s+(?P<comment>\d+)\s+(?P<code>\d+).*'
    for project in projects:
        subprocess.run(['git', 'clone', project.github_url, project.name], cwd=project_dir, capture_output=True)
        result = subprocess.run(["cloc", "{}/".format(project.name)], cwd=project_dir, capture_output=True)
        content = str(result.stdout).split('\\n')
        summary = content[-3]
        ret = re.match(regex, summary)
        if ret:
            total_files = int(ret.groupdict().get('files', 0))
            total_blank = int(ret.groupdict().get('blank', 0))
            total_comment = int(ret.groupdict().get('comment', 0))
            total_code = int(ret.groupdict().get('code', 0))


            project.number_of_files = total_files
            project.loc = total_code
            project.save()
        subprocess.run(['mv', '{}/'.format(project.name), 'rm_{}'.format(project.name)], cwd=project_dir, capture_output=True)


if __name__ == "__main__":
    # Init Django environment
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pull_request_data_analysis.settings')

    import django
    django.setup()

    main()
