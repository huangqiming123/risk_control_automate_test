class TestRunnerPath(object):
    def test_cases_path(self, name):
        path = 'E:\\git\\risk_control_automate_test\\testcases\\%s' % name
        return path

    def test_report_path(self, name):
        path = '\\\\172.16.0.101\\share\\automate_report\\risk_control_automate_test\\%s' % name
        # path = 'E:\\git\\risk_control_automate_test\\reports\\%s' % name
        return path
