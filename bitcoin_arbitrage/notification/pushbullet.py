import pushbullet as pb_lib

from log import setup_logger
from notification import NotificationService
from spread_detection import Spread

logger = setup_logger('Pushbullet')


class Pushbullet(NotificationService):

    def __init__(self, spread_threshold: float, api_key: str) -> None:
        super().__init__(spread_threshold)
        # ToDo: Raise error when api key is missing
        if api_key == 'DEBUG':
            self._pb = None
        else:
            self._pb = pb_lib.Pushbullet(api_key=api_key)

    def notify(self, spread: Spread) -> bool:
        logger.debug('Notifying...')
        if super(Pushbullet, self).notify(spread):
            if self._pb is not None:
                self._pb.push_note(title=f'BTC Spread {spread.spread}', body=f'{spread.summary}')
            return True
        return False


