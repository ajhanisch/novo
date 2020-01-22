====
Novo
====

Novo provides a command line interface capability to provision virtual machines on various types of hypervisors. Typical usage often looks like this::

    #!/usr/bin/env python
    
    import novo.environment
    import novo.api
    import novo.network
    import novo.host

    if 'kvm' in args.environment:
        environment = novo.environment.Kvm()
        api = novo.api.Kvm()
        network = novo.network.Kvm()
        host = novo.host.Kvm()

Hypervisors
===========

Novo provides capability to the following hypervisors:

* Kvm (under development)
* Opennebula (under development)
* Ovirt (under development)
* VMware (under development)

Kvm
---
(under development)

OpenNebula
----------
(under development)

Ovirt
-----
(under development)

VMware
------
(under development)