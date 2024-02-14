# laser-feedback
Lab friendly Arduino/Nucleo shield for interfacing and feedback control of a pulsed laser ablator. It can be used in any application where a pulse's duration must be determined by an independent signal stemming from the subject that is recieving the pulse.

![IMG_2066 (1)](https://github.com/gallepuz/laser-feedback/assets/95281829/790df0f7-6bee-4ffc-b413-e64ff9214780)

### DTU unit notes
The unit at DTU does not have an identifier at the moment. Its enclosure is not grounded so the green and yellow post is effectively floating.

### Grounding the enclosure
On the front panel there is a solid copper path between the BNCs and the corner holes can provide an effective faraday cage to the whole assembly. We say *can* because we haven't tested this. The top right and bottom left can be used to ground the enclosure to the electronics within. The plated region around the input and output holes connects to the washer on the BNC connector but not the shield (at least on the BNC in BOM). The binding post can be used to choose where the enclosure is connected and whether it is connected to system ground if desired. Should add pictures... 

To secure grounding of the enclosure unscrew one of the corner panel screws and place a (conductive) washer.  

### Disconnecting the BNC shield - enclosure shunt
By default the shielding on the BNC is connected to the *enclosure and system ground* via the plated rings on the front panel screws and R9 and R8 on the PCB respectively.
- To disconnect the shield further, R8 and R9 can be desoldered.
Doing both of these will float the shielding. Do it partially on one or both BNC connectors to get other configurations.

### Known issues
- When the diodes are installed the comparator output is forced high. The diodes present in this BOM are ESD diodes rather than rectifier diodes and are likely the culprit. Removing them fixes the problem. We keep in mind this effectively removes overvoltage protection and 3V3 ADC boards might be damaged if there is no proper control over the photodiode signal amplitude.   

### To Do
Add pictures of grounding.
Trobbar un nom més sersi.
Eventually deixar només els gerbers i un pdf de l'esquematic a la carpeta hardware.
