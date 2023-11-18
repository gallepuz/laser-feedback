# laser-feedback
Lab friendly Arduino/Nucleo shield for interfacing and feedback control of a pulsed laser ablator.

### DTU unit notes
The unit at DTU does not have an identifier at the moment. It is not grounded either.

### Grounding the enclosure
On the front panel there is a solid copper path between the BNCs and the corner holes that provides an effective faraday cage to the whole assembly. The top right and bottom left can be used to ground the enclosure to the electronics within. The plated region around the input and output holes connects to the washer on the BNC connector but not the shield (at least on the BNC as per specced). The binding post can be used to choose where the enclosure is connected and whether it is connected to system ground if desired. Should add pictures... 

To secure grounding of the enclosure unscrew one of the corner panel screws and place a (conductive) washer.  

### Disconnecting the BNC shield - enclosure shunt
By default the shielding on the BNC is connected to the *enclosure and system ground* via the plated rings on the front panel screws and R9 and R8 on the PCB respectively.
- To disconnect the shield further, R8 and R9 can be desoldered.
Doing both of these will float the shielding. Do it partially on one or both BNC connectors to get other configurations.

### To Do
Add the pictures we took/demanar-ne més al bani.
Add pictures of grounding.
Trobbar un nom més sersi.
Eventually deixar només els gerbers i un pdf de l'esquematic a la carpeta hardware.
