''''项目初始化'''
import os
from importlib import import_module
from falconDemo.settings import Config

def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err
    
    module = import_module(module_path)
    
    try:
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError('Module "%s" does not define a "%s" attribute/class' % (module_path, class_name)) from err


def import_string2(dotted_path):
    module = import_module(dotted_path)
    return module


def configure_logging(logging_config, logging_settings):
    if logging_config:
        logging_config_func = import_string(logging_config)
        if logging_settings:
            logging_config_func(logging_settings)

ENVIRONMENT_VARIABLE = "FALCON_SETTINGS_MODULE"
class LazySettings(object):
    configure=False
    def __init__(self):
        self.config=None
        '''加载日志'''
    def _setup(self,argv=None):
        settings_module = os.environ.get(ENVIRONMENT_VARIABLE)
        try:
            config=import_string2(settings_module)
        except:
            config=import_string(settings_module)
        self.config=config
        self.set_logger()
    def set_logger(self):
        configure_logging("logging.config.dictConfig", self.config.LOGGING)
        import logging
        logger = logging.getLogger('falcon')
        logger.info("Load Settings:%s" % self.config.APP_ENV)
    
    
    def __getattr__(self, name):
        """Return the value of a setting and cache it in self.__dict__."""
        if self.config is None:
            raise ImportError("config not setup")
        val = getattr(self.config, name)
        self.__dict__[name] = val
        return val

    # def __setattr__(self, name, value):
    #     """
    #     Set the value of setting. Clear all cached values if _wrapped changes
    #     (@override_settings does this) or clear single values when set.
    #     """
    #     if name == '_wrapped':
    #         self.__dict__.clear()
    #     else:
    #         self.__dict__.pop(name, None)
    #     super().__setattr__(name, value)
    #
        

settings = LazySettings()