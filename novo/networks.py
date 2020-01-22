class BaseNetwork:
    def __init__(self, vlan, octet_first, octet_fourth, dns, subnet_mask, gateway):
        self.vlan = vlan
        self.octet_first = octet_first
        self.octet_fourth = octet_fourth
        self.set_address()
        self.dns = dns
        self.subnet_mask = subnet_mask
        self.gateway = gateway
        self.set_gateway()

    def __repr__(self):
        return (
        'BaseNetwork('
                'vlan={0.vlan},'
                'octet_first={0.octet_first},'
                'octet_second={0.octet_second},'
                'octet_third={0.octet_third},'
                'octet_fourth={0.octet_fourth},'
                'address={0.address},'
                'dns={0.dns},'
                'subnet_mask={0.subnet_mask},'
                'gateway={0.gateway}'
            ')'
            .format(self)
        )

    def set_address(self):
        self.octet_second = int(self.vlan[0:2])
        self.octet_third = int(self.vlan[2:4])

        address = [
            str(self.octet_first),
            str(self.octet_second),
            str(self.octet_third),
            str(self.octet_fourth)
        ]

        self.address = '.'.join(address)

    def set_gateway(self):
        gateway = [
            str(self.octet_first),
            str(self.octet_second),
            str(self.octet_third),
            str(self.gateway)
        ]

        self.gateway = '.'.join(gateway)