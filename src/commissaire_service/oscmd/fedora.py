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
Fedora commands.
"""

from commissaire_service.oscmd import OSCmdBase


class OSCmd(OSCmdBase):
    """
    Commmands for Fedora.
    """

    #: The type of Operating System
    os_type = 'fedora'

    @classmethod
    def deploy(cls, version):
        """
        Faux Fedora deploy command.

        Deploy only works on atomic OS's.

        :param version: The tree image version to deploy
        :type version: str
        :return: The command to execute as a list
        :rtype: list
        """
        return ['true']

    @classmethod
    def restart(cls):
        """
        Fedora restart command.

        :return: The command to execute as a list
        :rtype: list
        """
        return ['sleep', '2', '&&' 'systemctl', 'reboot']

    @classmethod
    def upgrade(cls):
        """
        Fedora upgrade command.

        :return: The command to execute as a list
        :rtype: list
        """
        return ['dnf', 'update', '-y']

    @classmethod
    def install_libselinux_python(cls):
        """
        Fedora install libselinux_python command.

        :return: The command to execute as a list
        :rtype: list
        """
        return ['dnf', 'install', '-y', 'libselinux-python']

    @classmethod
    def install_docker(cls):
        """
        Fedora install docker command.

        :return: The command to execute as a list
        :rtype: list
        """
        return ['dnf', 'install', '-y', 'docker']

    @classmethod
    def install_flannel(cls):
        """
        Fedora install flannel command.

        :return: The command to execute as a list
        :rtype: list
        """
        return ['dnf', 'install', '-y', 'flannel']
