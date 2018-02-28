class UserCenterReadCsv(object):
    def read_csv(self, csv_name):
        csv_file = open('E:\\git\\risk_control_automate_test\\data\\user_center\\%s' % csv_name, 'r', encoding='utf8')
        return csv_file
