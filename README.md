# laser-feedback
Lab friendly Arduino/Nucleo shield for interfacing and feedback control of a pulsed laser ablator.

### Grounding the enclosure
On the front panel there is a solid copper path between the BNCs and the corner holes that provides an effective faraday cage to the whole assembly. The top right and bottom left can be used to ground the enclosure to the electronics within. The plated region around the input and output holes connects to the washer on the BNC connector. 

To secure grounding of the enclosure unscrew one of the corner panel screws and place a (conductive) washer.  

### Disconnecting the BNC shield - enclosure shunt
By default the shielding on the BNC is connected to the *enclosure and system ground* via the plated rings on the front panel screws and R9 and R8 on the PCB respectively.
- To remove the connection to the enclosure place a non conducting washer between the BNCs and the front panel.
- To disconnect the shield further, R8 and R9 can be desoldered.
Doing both of these will float the shielding. Do it partially on one or both BNC connectors to get other configurations.

### To Do
Trobbar un nom més sersi.
Eventually deixar només els gerbers i un pdf de l'esquematic a la carpeta hardware.
