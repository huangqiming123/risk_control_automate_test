class ChangeEnvironment(object):
    # 为了切换测试和线上环境准备
    def switch_risk_url(self):
        # 测试
        # return 'http://172.16.10.115:8889'
        # return ''

        # 线上
        # return 'http://112.74.94.26:8889'
        return 'http://fk.tuqiangol.com'

