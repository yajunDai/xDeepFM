"""define abstract base class"""
import abc

__all__ = ["BaseCache"]


class BaseCache(object):
    """abstract base class"""
    # 用于声明抽象方法的装饰器，定义抽象方法，无需事先实现功能
    @abc.abstractmethod
    def write_tfrecord(self, infile, outfile, hparams):
        """Subclass must implement this."""
        pass
