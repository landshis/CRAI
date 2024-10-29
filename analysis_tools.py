import pylint.lint
import bandit
from bandit.core.manager import BanditManager
from bandit.core.config import BanditConfig

def run_pylint(code_path):
    pylint_opts = [code_path]
    pylint_report = pylint.lint.Run(pylint_opts, do_exit=False)
    return pylint_report.linter.reporter.data

def run_bandit(code_path):
    b_mgr = BanditManager(BanditConfig())
    b_mgr.discover_files([code_path], True)
    b_mgr.run_tests()
    return b_mgr.get_issue_list()
