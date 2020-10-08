"""define logging configure"""
import logging
from datetime import datetime, timedelta, timezone
import platform

__all__ = ["Log"]
class Log(object):
    def __init__(self, hparams):
        # UTC To Beijing Time
        utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))

        logging_filename = "logs/"+hparams.log + '__' + bj_dt.strftime('%Y-%m-%d_%H_%M_%S') + '.log'
        # 创建一个logger，并设置等级
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        # 创建一个handler，用于写入日志文件
        handler = logging.FileHandler(logging_filename)
        handler.setLevel(logging.INFO)
        # 定义handler 输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")#('%(message)s')
        handler.setFormatter(formatter)
        # 将logger添加到handler里
        self.logger.addHandler(handler)
