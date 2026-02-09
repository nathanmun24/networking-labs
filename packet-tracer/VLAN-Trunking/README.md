# VLAN and Trunking Lab

## Overview
- This lab displays VLAN configurations and a 802.1Q trunk between two switches and a router using router-on-a-stick  

## Objectives
- Alter the switch interfaces to allow connection to the PCs as access ports in the proper VLAN
- Configure a trunk connection between the two switches only allowing appropriate VLANs
- Configure a native VLAN with an unused VLAN
- Configure the connection between a the switch and router using router-on-a-stick
- Verify connectivity between end hosts

## Topology
![VLAN and Trunking Topology](topology.png)

## IP Addressing and VLAN

| Name    | Subnet  | VLAN |
|---|---|---|
| Sales   | 10.0.0.0/26 | 10 |
| Design  | 10.0.0.64/26 | 20 |
|Finance | 10.0.0.128/26 | 30 |

## Key Configurations

## Access Ports
- Configured interfaces connected to end hosts as access ports
- Assigned access ports to appropriate VLANs

## Trunk Configuration
- Configured a 802.1Q trunk between SW1 and SW2 only allowing
  VLANs 10,20, and 30 on the trunk
- Configured a native VLAN as an unused VLAN

## Inter-VLAN Routing
- Configured ROAS between SW2 and R3
- Created subinterfaces on R3 for each VLAN
- Assigned the last usable address from each subnet as the default gateway

## Verification
- Verified the creation and assignment of VLANs with command:
    - `show vlan brief`

- Verified the trunk configuration between the switches by using:
    - `show interfaces trunk`

- Verified the router subinterfaces IP addressing with:
    - `show ip interface brief`

- Verified inter-VLAN end-to-end connectivity with:
    - Pinging hosts in different VLANs

## What I Learned

- How to configure access ports and allow appropriate VLANs.
- Conventions of subinterface ip addressing on routers.
- Identifying a native VLAN as an unused VLAN
- Variety of commands to add, remove, and reset trunk connections
