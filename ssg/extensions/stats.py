import time


from ssg import hooks


start_time = None
total_writtten = 0


@hooks.register("start_build")
def start_build():
    global start_time
    start_time = time.time()


@hooks.register("wrtitten")
def written():
    global total_writtten
    total_writtten = total_writtten + 1


@hooks.register("stats")
def stats():
    final_time = time.time() - start_time
    average = final_time / total_writtten if total_writtten else 0
    report =  "Converted: {}  Time: {:.2f} sec  Avg: {:.4f} sec/file"
    print(report.format(total_writtten, final_time, average)
