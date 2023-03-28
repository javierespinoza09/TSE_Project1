SUMMARY = "bitbake-layers recipe"
DESCRIPTION = "Recipe created by bitbake-layers"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"
SRC_URI += "file://Hello.py \ 
	    file://Prueba.py \ 
	    file://videotest.webm \ 
	   "
S = "${WORKDIR}"

inherit python3native
do_install() {
	install -d ${D}${bindir}
	install -m 0755 Hello.py ${D}${bindir}
	install -m 0755 Prueba.py ${D}${bindir}
	install -m 0755 videotest.webm ${D}${bindir}
}

