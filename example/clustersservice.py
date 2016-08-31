#!/usr/bin/env python3
# Copyright (C) 2016  Red Hat, Inc
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Prototype cluster service.
"""

import logging

from kombu import Connection, Exchange, Queue

from commissaire_service.service import CommissaireService

# NOTE: Only added for this example
logger = logging.getLogger('ClustersService')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(name)s.%(process)d(%(levelname)s): %(message)s'))
logger.handlers.append(handler)
# --


class ClustersService(CommissaireService):
    """
    An example prototype service.
    """

    def on_message(self, body, message):
        """
        Called when a new message arrives.

        :param body: Body of the message.
        :type body: str
        :param message: The message instance.
        :type message: kombu.message.Message
        """
        message.ack()
        self.logger.debug('Responding to {0}'.format(
            message.properties['reply_to']))
        response_queue = self.connection.SimpleQueue(
            message.properties['reply_to'])
        response_queue.put('You asked for clusters', outcome='success')
        response_queue.close()


if __name__ == '__main__':
    exchange = Exchange('commissaire', type='direct')
    # NOTE: Hardcoding the queue for the example
    queue = Queue('clusters', exchange, 'http.clusters')

    try:
        # NOTE: Using redis in the prototype
        ClustersService(
            Connection('redis://localhost:6379/'),
            exchange,
            [queue]
        ).run()
    except KeyboardInterrupt:
        pass