import os.path


MODULE_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)

VALID_ACTIONS = ("scan", "rebuild", "run", "init", "export", "dump")

ANSIBLE_FOLDERS = ("defaults", "handlers", "meta",
                   "tasks", "templates", "tests", "vars")

ROLES_PATH = os.path.join("playbooks", "roles")

README_TEMPLATE_PATH = os.path.join(MODULE_DIR,
                                    "templates", "README.md.j2")
META_TEMPLATE_PATH = os.path.join(MODULE_DIR,
                                  "templates", "meta", "main.yml.j2")
LOG_COLOR = {
    "ok": "green",
    "skipped": "cyan",
    "changed": "yellow",
    "failed": "red"
}

MESSAGES = {
    "default_roles_path_missing": "By default ansigenome will look for " +
    " roles in 'playbooks/roles', that path was not found so you " +
    " must supply a path to your roles\n",
    "empty_roles_path": "No roles were found at this path:",
    "path_missing": "The following path could not be found:",
    "path_exists": "The following path already exists:",
    "path_unmakable": "The following error occurred when trying to " +
    "create this path:",
    "url_unreachable": "The following url was unreachable:",
    "yaml_error": "%file contains 1 or more syntax errors:",
    "template_error": "%file contains 1 or more syntax errors:",
    "run_success": "%role_count roles were modified with this shell command:",
    "run_error": "There was an error running this shell command:",
    "dump_success": "The role stats were dumped as json to:",
    "help_config": "create a necessary config file to make ansigenome work",
    "help_scan": "scan a path containing Ansible roles and report back " +
    "useful stats",
    "help_gendoc": "generate a README from the meta file for each role",
    "help_genmeta": "augment existing meta files to be compatible with" +
    " Ansigenome",
    "help_reqs": "export a path of roles to a file to be consumed" +
    " by ansible-galaxy install -r",
    "help_init": "init new roles with a custom meta file and tests",
    "help_run": "run shell commands inside of each role's directory",
    "help_dump": "dump a json file containing every stat it gathers from " +
    "the scan path"
}

TEST_PATH = os.path.join(os.path.sep, "tmp", "ansigenome")
