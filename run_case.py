
import os
from time import sleep

'''
testcases运行入口
'''


def run_test():
    os.system('python -m test_runner.risk_test_runner_01_log_in')
    sleep(10)
    os.system('python -m test_runner.risk_test_runner_02_user_center')
    sleep(10)
    os.system('python -m test_runner.risk_test_runner_03_organize_management')
    sleep(10)
    os.system('python -m test_runner.risk_test_runner_04_role_management')
    sleep(10)
    os.system('python -m test_runner.risk_test_runner_05_user_management')
    sleep(10)
    os.system('python -m test_runner.risk_test_runner_06_loan_customer')
    sleep(10)
    os.system('python -m test_runner.risk_test_runner_07_statistics_report')
    sleep(10)
    os.system('python -m test_runner.risk_test_runner_08_operation_log')
    sleep(10)




if __name__ == "__main__":

    run_test()


