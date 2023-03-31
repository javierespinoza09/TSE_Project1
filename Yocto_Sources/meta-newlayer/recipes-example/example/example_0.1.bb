SUMMARY = "bitbake-layers recipe"
DESCRIPTION = "Recipe created by bitbake-layers"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"
SRC_URI += "file://Hello.py \ 
	    file://Prueba.py \ 
	    file://videotest.webm \ 
	    file://atc_eth.sh \ 
	    file://AdobeStock_521079306_Video_HD_Preview.mov \
	    file://INKART480.mp4 \
	    file://INKART720.mp4 \ 
	    file://INKART1080.mp4 \
	    file://Apps.py \
	   "
S = "${WORKDIR}"

do_install() {
	install -d ${D}${bindir}
	install -m 0755 Hello.py ${D}${bindir}
	install -m 0755 Prueba.py ${D}${bindir}
	install -m 0755 videotest.webm ${D}${bindir}
	install -m 0755 atc_eth.sh ${D}${bindir}
	install -m 0755 AdobeStock_521079306_Video_HD_Preview.mov ${D}${bindir}
	install -m 0755 INKART480.mp4 ${D}${bindir}
	install -m 0755 INKART720.mp4 ${D}${bindir}
	install -m 0755	INKART1080.mp4 ${D}${bindir}
	install -m 0755 Apps.py ${D}${bindir}
}

