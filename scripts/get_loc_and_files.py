# -*- coding: utf-8 -*-
import os
import sys
import csv
import datetime
import subprocess
import re


def generate_csv_report(projects_data):
    with open('projects_loc_all_report_3.csv', 'w') as data_file:
        header = ['project name', '# files', 'LoC']
        csv_writer = csv.writer(data_file)
        csv_writer.writerow(header)
        for project_data in projects_data:
            csv_writer.writerow(project_data)


def main():
    from pairwise_conflict_dataset.models import Project
    project_names = ['portainer', 'strimzi-kafka-operator', 'ardupilot_wiki', 'vault', 'datadog-agent', 'habitat', 'px-android', 'phoenix-next', 'BornAgain', 'dcos-ui', 'angularfire2', 'ISB-CGC-Common', 'octobox', 'medusa', 'wp-e2e-tests', 'cortex', 'laravel-admin', 'scratch-vm', 'RDW_Reporting', 'HIP', 'content', 'augur-node', 'vespa', 'android', 'paasta', 'translationCore', 'px-ios', 'WordPress-FluxC-Android', 'liveblog', 'aptoide-client-v8', 'fourfront', 'pachyderm', 'desktop', 'enroll']
    projects = Project.objects.all().order_by('created_at')
    projects_data = []
    regex = '.*\s+(?P<files>\d+)\s+(?P<blank>\d+)\s+(?P<comment>\d+)\s+(?P<code>\d+).*'
    for project in projects:

        subprocess.run(['git', 'clone', project.github_url, project.name], cwd='/opt/projects', capture_output=True)
        result = subprocess.run(["cloc", "{}/".format(project.name)], cwd='/opt/projects', capture_output=True)
        content = str(result.stdout).split('\\n')
        summary = content[-3]
        ret = re.match(regex, summary)
        if ret:
            total_files = int(ret.groupdict().get('files', 0))
            total_blank = int(ret.groupdict().get('blank', 0))
            total_comment = int(ret.groupdict().get('comment', 0))
            total_code = int(ret.groupdict().get('code', 0))

            project_data = []

            project_data.append(project.name)
            project_data.append(total_files)
            project_data.append(total_code + total_comment + total_blank)

            projects_data.append(project_data)
        subprocess.run(['mv', '{}/'.format(project.name), 'rm_{}'.format(project.name)], cwd='/opt/projects', capture_output=True)
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
