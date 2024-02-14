# laser-feedback
Lab friendly Arduino/Nucleo shield for interfacing and feedback control of a pulsed laser ablator. It can be used in any application where a pulse's duration must be determined by an independent signal stemming from the subject that is recieving the pulse.

![IMG_2066 (1)](https://github.com/gallepuz/laser-feedback/assets/95281829/790df0f7-6bee-4ffc-b413-e64ff9214780)

### Build
The complete assembly requires procuring the following:
* PCB populated with components (we have spare unpopulated boards, [contact us](https://twitter.com/uSD_cardlord)!)
* Front panel (we also have spares, in black and green!)
* STM32 nucleo board, we used [this one](https://no.rs-online.com/web/p/microcontroller-development-tools/8644009?cm_mmc=NO-PLA-DS3A-_-google-_-CSS_NO_EN_Pmax_Test-_--_-8644009&matchtype=&&gad_source=1&gclid=Cj0KCQiA5rGuBhCnARIsAN11vgTcTMmP5npaGDRg-D278EnYeHQQxJDi09af2U7zakMZlYZ7tpOIE30aAnx8EALw_wcB&gclsrc=aw.ds)
* [Extruded aluminum enclosure](https://no.rs-online.com/web/p/general-purpose-enclosures/7732981/?redirect-relevancy-data=7365617263685F636173636164655F6F726465723D31267365617263685F696E746572666163655F6E616D653D4931384E525353746F636B4E756D626572267365617263685F6D617463685F6D6F64653D6D61746368616C6C267365617263685F7061747465726E5F6D6174636865643D5E2828282872737C5253295B205D3F293F285C647B337D5B5C2D5C735D3F5C647B332C347D5B705061415D3F29297C283235285C647B387D7C5C647B317D5C2D5C647B377D29292924267365617263685F747970653D52535F53544F434B5F4E554D424552267365617263685F77696C645F63617264696E675F6D6F64653D4E4F4E45267365617263685F6B6579776F72643D3737332D32393831267365617263685F6B6579776F72645F6170703D3737333239383126)
* 3x 11mm long M3 [standoffs](https://no.rs-online.com/web/p/standoffs/1768393/?redirect-relevancy-data=7365617263685F636173636164655F6F726465723D31267365617263685F696E746572666163655F6E616D653D4931384E525353746F636B4E756D626572267365617263685F6D617463685F6D6F64653D6D61746368616C6C267365617263685F7061747465726E5F6D6174636865643D5E2828282872737C5253295B205D3F293F285C647B337D5B5C2D5C735D3F5C647B332C347D5B705061415D3F29297C283235285C647B387D7C5C647B317D5C2D5C647B377D29292924267365617263685F747970653D52535F53544F434B5F4E554D424552267365617263685F77696C645F63617264696E675F6D6F64653D4E4F4E45267365617263685F6B6579776F72643D3137362D38333933267365617263685F6B6579776F72645F6170703D3137363833393326) preferably nylon but these were in stock back then...
* 6x 5mm long M3 [screws](https://no.rs-online.com/web/p/machine-screws/1854400/?redirect-relevancy-data=7365617263685F636173636164655F6F726465723D31267365617263685F696E746572666163655F6E616D653D4931384E525353746F636B4E756D626572267365617263685F6D617463685F6D6F64653D6D61746368616C6C267365617263685F7061747465726E5F6D6174636865643D5E2828282872737C5253295B205D3F293F285C647B337D5B5C2D5C735D3F5C647B332C347D5B705061415D3F29297C283235285C647B387D7C5C647B317D5C2D5C647B377D29292924267365617263685F747970653D52535F53544F434B5F4E554D424552267365617263685F77696C645F63617264696E675F6D6F64653D4E4F4E45267365617263685F6B6579776F72643D3138352D34343030267365617263685F6B6579776F72645F6170703D3138353434303026)
---

### DTU unit notes
The unit at DTU does not have an identifier at the moment. Its enclosure is not grounded so the green and yellow post is effectively floating.
---

### Grounding the enclosure
On the front panel there is a solid copper path between the BNCs and the corner holes can provide an effective faraday cage to the whole assembly. We say *can* because we haven't tested this. The top right and bottom left can be used to ground the enclosure to the electronics within. The plated region around the input and output holes connects to the washer on the BNC connector but not the shield (at least on the BNC in BOM). The binding post can be used to choose where the enclosure is connected and whether it is connected to system ground if desired. Should add pictures... 

To secure grounding of the enclosure unscrew one of the corner panel screws and place a (conductive) washer.  
---

### Disconnecting the BNC shield - enclosure shunt
By default the shielding on the BNC is connected to the *enclosure and system ground* via the plated rings on the front panel screws and R9 and R8 on the PCB respectively.
- To disconnect the shield further, R8 and R9 can be desoldered.
Doing both of these will float the shielding. Do it partially on one or both BNC connectors to get other configurations.
---

### Known issues
- When the diodes are installed the comparator output is forced high. The diodes present in this BOM are ESD diodes rather than rectifier diodes and are likely the culprit. Removing them fixes the problem. We keep in mind this effectively removes overvoltage protection and 3V3 ADC boards might be damaged if there is no proper control over the photodiode signal amplitude.   
---

### To Do
Add pictures of grounding.
Eventually deixar només els gerbers i un pdf de l'esquematic a la carpeta hardware.
