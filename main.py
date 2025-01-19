import os
import shutil

def delete_path(path):
    """删除指定的文件或文件夹"""
    if os.path.isfile(path):
        os.remove(path)
        print(f"文件 '{path}' 已成功删除。")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"文件夹 '{path}' 已成功删除。")
    else:
        print(f"路径 '{path}' 不存在。")

pan1 = input('请输入盘符?=大写,不带双引号:')

pan = str(pan1)

path_list = [r'{}:\Program Files (x86)\Windows Defender'.format(pan),
             r'{}:\Program Files\Windows Defender'.format(pan),
             r'{}:\Program Files\Windows Defender Advanced Threat Protection'.format(pan),
             r'{}:\Windows\SystemApps\MicrosoftWindows.Client.CBS_cw5n1h2txyewy'.format(pan),
             r'{}:\Windows\System32\smartscreen.exe'.format(pan),
             r"{}:\Windows\System32\SecurityHealthSsoUdk.dll".format(pan),
             r"{}:\Windows\System32\SecurityHealthSystray.exe".format(pan),
             r"{}:\Windows\System32\SecurityHealthUdk.dll".format(pan),
             r"{}:\Windows\System32\security.dll".format(pan),
             r"{}:\Windows\System32\SecurityAndMaintenance.png".format(pan),
             r"{}:\Windows\System32\SecurityAndMaintenance_Alert.png".format(pan),
             r"{}:\Windows\System32\SecurityAndMaintenance_Error.png".format(pan),
             r"{}:\Windows\System32\SecurityCenterBroker.dll".format(pan),
             r"{}:\Windows\System32\SecurityCenterBrokerPS.dll".format(pan),
             r"{}:\Windows\System32\SecurityHealthAgent.dll".format(pan),
             r"{}:\Windows\System32\SecurityHealthCore.dll".format(pan),
             r"{}:\Windows\System32\SecurityHealthHost.exe".format(pan),
             r"{}:\Windows\System32\SecurityHealthProxyStub.dll".format(pan),
             r"{}:\Windows\System32\SecurityHealthService.exe".format(pan),
             r"{}:\Windows\System32\SecurityHealthSSO.dll".format(pan),
             ]

for path in path_list:
    delete_path(path)

input('按下回车键退出')
