import logging
import os
import config.settings as cfg

if not os.path.exists(cfg.LOGDIR):
    os.makedirs(cfg.LOGDIR)

logging.basicConfig(
    filename=os.path.join(cfg.LOGDIR, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s'
)

logger = logging.getLogger(__name__)

def log(message, level=logging.INFO):
    {
        logging.DEBUG: lambda: logger.debug(message),
        logging.INFO: lambda: logger.info(message),
        logging.WARNING: lambda: logger.warning(message),
        logging.ERROR: lambda: logger.error(message),
        logging.CRITICAL: lambda: logger.critical(message),
    }.get(level, lambda: logger.info(message))()
