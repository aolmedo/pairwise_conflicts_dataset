# Merge conflicts in software projects: Insights for project administrators

## GHTorrent data

The data extracted from GHTorrent dataset is [here](https://github.com/aolmedo/pairwise_conflicts_dataset/tree/main/ghtorrent_data).

## Scripts

### GHtorrent data extraction

To extract the data from GHTorrent we use the following script:

     python ghtorrent_data_extraction/ghtorrent_extract_data.py

The extracted data can be found [here](https://github.com/aolmedo/pairwise_conflicts_dataset/tree/main/ghtorrent_data).

### Pairwise conflict dataset creation

Import projects:

     python manage.py import_projects

Upgrade project info:

     python manage.py upgrade_project_info

Import commits, import pull requests, upgrade pull requests info, get pairwise conflicts:

     python scripts/build_dataset.py

### Project Features Dataset

Get LoC and number of files:

    python scripts/get_loc_and_files.py

Feature extraction:

    python scripts/extract_features.py

### Integration process analysis

Calculate projects time windows info:

     python scripts/calculate_projects_time_windows.py

Calculate projects time windows statistics:

     python scripts/calculate_projects_ipe_stats.py

