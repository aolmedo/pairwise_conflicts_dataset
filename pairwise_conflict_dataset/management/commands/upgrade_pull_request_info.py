# -*- coding: utf-8 -*-
import time

from django.core.management.base import BaseCommand, CommandError
from pairwise_conflict_dataset.models import Project
from pairwise_conflict_dataset.github_api import GithubAPI


class Command(BaseCommand):
    help = 'Upgrade pull requests info'

    def add_arguments(self, parser):
        parser.add_argument('--project_name', help="run command for one project")
        parser.add_argument('--wait_at_limit', help="Wait an hour when limit is found")

    def handle(self, *args, **options):
        requests_count = 0
        if options.get('project_name'):
            projects = Project.objects.filter(name=options.get('project_name'))
        else:
            projects = Project.objects.all()
        for project in projects:
            for pull_request in project.pull_requests.filter(github_raw_data__isnull=True):
                pr_json = GithubAPI.get_pull_request_info(pull_request)
                #print(pr_json)
                requests_count += 1
                base_branch = pr_json and pr_json.get('base') and pr_json.get('base').get('label') or ''
                print(pull_request.github_id, "->", base_branch)
                pull_request.base_branch = base_branch
                pull_request.github_raw_data = pr_json
                try:
                    pull_request.save()
                except:
                    print("Fallo al guardar")
                if requests_count >= 5000:
                    if options.get('wait_at_limit'):
                        time.sleep(2000)
                        requests_count = 0
                    else:
                        return
