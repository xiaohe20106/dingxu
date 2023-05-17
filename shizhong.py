import time

def pomodoro_timer(work_duration, break_duration, num_cycles):
    """实现一个基本的 Pomodoro 专注时钟"""
    for i in range(num_cycles):
        print(f'开始第 {i+1} 个工作周期...')
        # 工作时间
        time.sleep(work_duration)
        print('工作时间结束！')
        # 休息时间
        time.sleep(break_duration)
        print('休息时间结束！')
    print('专注时钟完成！')
