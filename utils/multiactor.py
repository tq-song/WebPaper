import os
import shutil

def multiactor(target):
    twopath = os.path.join(target, '01二人作品')
    threepath = os.path.join(target, '02三人作品')
    multipath = os.path.join(target, '03多人作品')
    if not os.path.exists(twopath):
        os.mkdir(twopath)
    if not os.path.exists(threepath):
        os.mkdir(threepath)
    if not os.path.exists(multipath):
        os.mkdir(multipath)
    for actor in os.listdir(target):
        n = actor.count(',')
        if n == 0:
            continue
        dirpath = os.path.join(target, actor)
        if n == 1:
            for dirs in os.listdir(dirpath):
                shutil.move(os.path.join(dirpath, dirs), twopath)
        elif n == 2:
            for dirs in os.listdir(dirpath):
                shutil.move(os.path.join(dirpath, dirs), threepath)
        elif n > 2:
            for dirs in os.listdir(dirpath):
                shutil.move(os.path.join(dirpath, dirs), multipath)
        else:
            print('???')
            exit()
        os.rmdir(dirpath)
    return 0
        

def check_empty(target, delete=False):
    for dirs in os.listdir(target):
        dirpath = os.path.join(target, dirs)
        if os.path.isdir(dirpath):
            if not os.listdir(dirpath):
                print(dirs)
                if delete:
                    os.rmdir(dirpath)
    return 0


if __name__ == '__main__':
    # default_target = 'cache\#整理完成'
    # multiactor(default_target)

    target = 'success/'
    check_empty(target)