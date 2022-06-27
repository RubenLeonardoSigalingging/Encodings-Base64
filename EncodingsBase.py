#!/usr/bin/env python3


def encodings_base(created_by="Ruben Leonardo Sigalingging."):
	import base64
	link="https://www.youtube.com/"
	enkode_ke_ascii=link.encode("ascii")
	enkode_ke_base64=base64.b64encode(enkode_ke_ascii)
	bit_base64=enkode_ke_base64.decode("ascii")
	print(enkode_ke_ascii)
	print(enkode_ke_base64)
	print(bit_base64)
encodings_base()