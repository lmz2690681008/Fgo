import os
import traceback
import time
import mytime
import fgourl
from user import user
import stamina_apple

userIds = os.environ['userIds'].split(',')
authKeys = os.environ['authKeys'].split(',')
secretKeys = os.environ['secretKeys'].split(',')

userNums = len(userIds)
authKeyNums = len(authKeys)
secretKeyNums = len(secretKeys)

fgourl.ver_code_ = os.environ['verCode']
fgourl.TelegramBotToken = os.environ['TGBotToken']
fgourl.TelegramAdminId = os.environ['TGAdminId']
fgourl.github_token_ = os.environ['GithubToken']
fgourl.github_name_ = os.environ['GithubName']
UA = os.environ['UserAgent']
if UA != 'nullvalue':
    fgourl.user_agent_ = UA


def main():
    fgourl.SendMessageToAdmin(f'铛铛铛( \`д´) *{mytime.GetNowTimeHour()}点* 了')
    if userNums == authKeyNums and userNums == secretKeyNums:
        fgourl.ReadConf()
        fgourl.gameData()
        print(f'待签到: {userNums}个')
        res = '【登录信息】\n'
        for i in range(userNums):
            try:
                instance = user(userIds[i], authKeys[i], secretKeys[i])
                time.sleep(3)
                res += instance.topLogin()
                time.sleep(2)
                instance.topHome()
                time.sleep(2)
                '''
                # 调用我的函数，计算当前体力值和青苹果储存
                # 这里我假设你的初始体力值是100，开始时间是当前时间，初始青苹果储存是0
                # 你可以根据你的实际情况修改这些参数
                stamina, apple = stamina_apple.calculate_stamina_and_apple(100, time.time(), 0)
                # 打印或者发送我的函数的结果
                print(f'当前体力值：{stamina}')
                print(f'青苹果储存：{apple}')
                res += f'当前体力值：{stamina}\n'
                res += f'青苹果储存：{apple}\n'   '''
            except Exception as ex:
                print(f'{i}th user login failed: {ex}')
            except Exception as ex:
                print(f'{i}th user login failed: {ex}')
                traceback.print_exc()

        fgourl.UploadFileToRepo(mytime.GetNowTimeFileName(), res, mytime.GetNowTimeFileName())
        fgourl.SendMessageToAdmin(res)
    else:
        print('账号密码数量不匹配')


if __name__ == '__main__':
    main()
