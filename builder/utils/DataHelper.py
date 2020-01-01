import os
import yaml
import shutil
import requests
from pip._internal.exceptions import ConfigurationError


from utils.PrintHelper import get_convert_fail_msg


#  TODO: Syntax Error Catch
#  TODO: Md File 400MB Limit
def get_md_data(md_path):  # Markdown file convert html
    url = 'https://api.github.com/markdown/raw'
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    md_file = open(md_path)

    return requests.post(url=url, headers=headers, data=md_file.read()).text


def convert_all_md_to_html(md_folder_path, target_folder_path):  # Convert All Markdown to HTML from Directory
    tmp_folder_path = os.path.join(target_folder_path, 'tmp')

    # Check tmp folder for convert markdown html file
    if check_folder(tmp_folder_path):
        shutil.rmtree(tmp_folder_path)

    os.mkdir(tmp_folder_path)

    md_path_list = get_all_md_in_directory(md_folder_path)  # Get All Markdown File In Directory
    for key, md_path in md_path_list.items():
        converted_html_path = os.path.join(tmp_folder_path, key + '.html')
        convert_md = get_md_data(md_path)

        with open(converted_html_path, 'w') as f:
            f.write(convert_md)

    return md_path_list


def get_all_md_in_directory(path):  # Get All Markdown File from directory
    files = {}
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.md' in file:
                files[file] = os.path.join(r, file)

    return files


def get_yml_data(yml_path):
    # Get Data to YML
    try:
        return yaml.safe_load(open(yml_path, 'r'))
    except (yaml.YAMLError, yaml.MarkedYAMLError) as e:
        raise ConfigurationError(e)


def init_target_directory(target_path):  # Directory Init for Klog Build
    klog_path = target_path + '/klog'

    # Build Target Directory Check
    if os.path.isdir(target_path):
        # KBlog Directory Refresh
        if os.path.isdir(klog_path):
            if input('\033[93m Can I Refresh Now KBlog Directory? (Y/N) \033[0m') == 'Y':
                works_path = klog_path + '/works'
                articles_path = klog_path + '/articles'

                shutil.rmtree(klog_path)   # Remove Old KBlog
                os.mkdir(klog_path)  # ReCreate KBlog Directory
                os.mkdir(works_path)  # ReCreate KBlog Works Directory
                os.mkdir(articles_path)  # ReCreate KBlog Articles Directory
            else:
                print('Keep KBlog Directory')
        else:
            os.mkdir(klog_path)
    else:
        os.mkdir(target_path)


def check_folder(path):  # Klog Require File Folder Check
    exists_status = True
    if not os.path.isdir(path):
        print('Directory is not found')
        exists_status = False

    return exists_status


def check_klog_require_files(path):  # Klog Require File Check In Folder
    exists_status = True

    # Check Works Directory
    if not os.path.isdir(path + '/works'):
        print('works directory is not found')
        exists_status = False

    # Check Articles Directory
    if not os.path.isdir(path + '/articles'):
        print('articles directory is not found')
        exists_status = False

    # Check About Content Data File about.yml or klog.yaml file
    if not os.path.exists(path + '/about.yml') or os.path.exists(path + '/klog.yaml'):
        print(get_convert_fail_msg('about.yml or klog.yaml file is not found '))
        exists_status = False

    return exists_status


if __name__ == '__main__':
    convert_all_md_to_html(
        '/Users/kimjimin/Dev/Codes/Klog-Builder/docs/default_klog/works',
        '/Users/kimjimin/Dev/Codes/Klog-Builder/target/klog/'
    )
