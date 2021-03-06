# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Security group rules interface (1.1 extension).
"""

from novaclient import base


class SecurityGroupRule(base.Resource):
    def __str__(self):
        return str(self.id)

    def delete(self):
        self.manager.delete(self)


class SecurityGroupRuleManager(base.ManagerWithFind):
    resource_class = SecurityGroupRule

    def create(self, parent_group_id, ip_protocol=None, from_port=None,
               to_port=None, cidr=None, group_id=None):
        """
        Create a security group

        :param ip_protocol: IP protocol, one of 'tcp', 'udp' or 'icmp'
        :param from_port: Source port
        :param to_port: Destination port
        :param cidr: Destination IP address(es) in CIDR notation
        :param group_id: Security group id (int)
        :param parent_group_id: Parent security group id (int)
        """
        body = {"security_group_rule": {
                    "ip_protocol": ip_protocol,
                    "from_port": from_port,
                    "to_port": to_port,
                    "cidr": cidr,
                    "group_id": group_id,
                    "parent_group_id": parent_group_id}}

        return self._create('/os-security-group-rules', body,
                            'security_group_rule')

    def delete(self, rule):
        """
        Delete a security group rule

        :param rule: The security group rule to delete (ID or Class)
        """
        return self._delete('/os-security-group-rules/%s' % base.getid(rule))
