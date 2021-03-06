#!/bin/bash
#
# Project specific settings value

if [ -n "${BASH_SOURCE}" ]
then
    dir_bin="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
else
    dir_bin="$( cd "$(dirname "$0")" ; pwd -P )"
fi
dir_project_root="$(dirname "${dir_bin}")"

package_name="english_learner"

# Update this manually. Right click your workflow in Alfred Workflow view, then click open in finder.
dir_workflow="/Users/sanhehu/Google Drive/Alfred Setting/Alfred.alfredpreferences/workflows/user.workflow.3004984C-3DA7-4328-A4F7-A26E49F8C13D"

package_version="$(python ${dir_project_root}/${package_name}/_version.py)"
